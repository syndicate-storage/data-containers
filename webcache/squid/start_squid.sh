#! /bin/bash
#   Copyright 2016 The Trustees of University of Arizona
#
#   Licensed under the Apache License, Version 2.0 (the "License" );
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

if [[ ! -d ${SQUID_CACHE_DIR}/00 ]]; then
    echo "Initialize Cache..."
    squid3 -N -f /etc/squid3/squid.conf -z
fi

echo "Run squid..."
squid3 -f /etc/squid3/squid.conf -NYCd 1
