#! /usr/bin/env python
"""
   Copyright 2016 The Trustees of University of Arizona

   Licensed under the Apache License, Version 2.0 (the "License" );
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
import json
import grequests
from math import radians, cos, sin, asin, sqrt


REPO_URL = "https://butler.opencloud.cs.arizona.edu/sdm/cdn_catalogue"


class RepositoryException(Exception):
    pass


class RepositoryEntryCDNSite(object):
    """
    repository entry - cdn site
    """
    def __init__(self, name, gps_loc, cdn_prefix):
        self.name = name
        self.gps_loc = gps_loc
        self.cdn_prefix = cdn_prefix

    @classmethod
    def from_dict(cls, ent):
        return RepositoryEntryCDNSite(
            ent["name"],
            ent["gps_loc"],
            ent["cdn_prefix"]
        )

    def to_json(self):
        return json.dumps({
            "name": self.name,
            "gps_loc": self.gps_loc,
            "cdn_prefix": self.cdn_prefix
        })

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "<RepositoryEntryCDNSite %s>" % \
            (self.name)


class RepositoryEntry(object):
    """
    repository entry
    """
    def __init__(self, dataset, ag_url, cdn_sites):
        self.dataset = dataset.strip().lower()
        self.ag_url = ag_url.strip()
        self.cdn_sites = cdn_sites

    @classmethod
    def from_json(cls, jsonstr):
        ent = json.loads(jsonstr)
        return cls.from_dict(ent)

    @classmethod
    def from_dict(cls, ent):
        cdn_sites = ent["cdn_sites"]
        cdn_sites_obj = []
        for cdn_site in cdn_sites:
            cdn_sites_obj.append(RepositoryEntryCDNSite.from_dict(cdn_site))

        return RepositoryEntry(
            ent["dataset"],
            ent["ag_url"],
            cdn_sites_obj
        )

    def to_json(self):
        return json.dumps({
            "dataset": self.dataset,
            "ag_url": self.ag_url,
            "cdn_sites": self.cdn_sites
        })

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return "<RepositoryEntry %s %s>" % \
            (self.dataset, self.ag_url)


class Repository(object):
    """
    Manage CDN Repository
    """
    def __init__(self, url):
        self.table = {}

        if not url:
            raise RepositoryException("not a valid repository url : %s" % url)

        self.load_table(url)

    def load_table(self, url):
        self.table = {}
        try:
            req = [grequests.get(url)]
            res = grequests.map(set(req))[0]
            ent_arr = res.json()
            for ent in ent_arr:
                entry = RepositoryEntry.from_dict(ent)
                self.table[entry.dataset] = entry
        except Exception, e:
            raise RepositoryException("cannot retrieve repository entries : %s" % e)

    def get_entry(self, dataset):
        k = dataset.strip().lower()
        if k in self.table:
            return self.table[k]
        return None

    def list_entries(self):
        entries = []
        for k in self.table.keys():
            entries.append(self.table[k])
        return entries


def ip_location():
    url = "http://ipinfo.io/json"

    req = [grequests.get(url)]
    res = grequests.map(set(req))[0]
    data = res.json()

    loc_arr = data["loc"].split(",")
    loc_val_arr = []
    for loc in loc_arr:
        loc_val_arr.append(float(loc))
    return loc_val_arr


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km


def haversine_arr(gps1, gps2):
    return haversine(gps1[0], gps1[1], gps2[0], gps2[1])


def find_closest_site(repo_entry, my_loc, verbose=False):
    ag_url = repo_entry.ag_url
    cdn_sites = repo_entry.cdn_sites

    min_dist = -1
    closest_site = None
    if verbose:
        print "dataset %s" % repo_entry.dataset

    for site in cdn_sites:
        dist = haversine_arr(my_loc, site.gps_loc)
        if verbose:
            print "%s ==> %d" % (site.name, dist)

        if min_dist < 0:
            min_dist = dist
            closest_site = site
        else:
            if min_dist > dist:
                min_dist = dist
                closest_site = site

    if verbose:
        print "closest site : %s ==> %d" % (closest_site.name, min_dist)
        print "prefix : %s" % (closest_site.cdn_prefix)
    return closest_site, min_dist


def make_akamai_plugin_conf(path, maps):
    cdn_maps = []
    for m in maps:
        dataset, ag_url, closest_site = m
        cdn_map_obj = {
            "host": ag_url,
            "cdn_prefix": closest_site.cdn_prefix
        }
        cdn_maps.append(cdn_map_obj)

    conf = {
        "DRIVER_WC_PLUGIN": "akamai",
        "DRIVER_WC_PLUGIN_CONFIG": {
            "akamai": {
                "map": cdn_maps
            }
        }
    }

    with open(path, "w") as f:
        json.dump(conf, f, indent=4, separators=(',', ': '))


def main(argv):
    repository = Repository(REPO_URL)
    loc = ip_location()
    #loc = [39.022867, -103.251398]

    repo_entries = repository.list_entries()

    maps = []
    for repo_entry in repo_entries:
        closest_site, dist = find_closest_site(repo_entry, loc, False)
        print "dataset: %s , closest_site: %s" % (repo_entry.dataset, closest_site)
        maps.append((repo_entry.dataset, repo_entry.ag_url, closest_site))

    if len(argv) > 0:
        conf_path = argv[0]
        make_akamai_plugin_conf(conf_path, maps)


if __name__ == "__main__":
    main(sys.argv[1:])
