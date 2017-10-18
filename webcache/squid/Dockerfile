# webcache-squid
#
# VERSION	1.0

FROM	ubuntu:14.04
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

##############################################
# Setup Squid
##############################################
ENV SQUID_VERSION 3.3.8
ENV SQUID_CACHE_DIR /var/spool/squid3
ENV SQUID_LOG_DIR /var/log/squid3
ENV SQUID_USER proxy

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 80F70E11F0F0D5F10CB20E62F5DA5F09C3173AA6 && \
    echo "deb http://ppa.launchpad.net/brightbox/squid-ssl/ubuntu trusty main" >> /etc/apt/sources.list

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends \
    squid3-ssl=${SQUID_VERSION}* && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt /var/lib/cache /var/lib/log

# make log dir
RUN mkdir -p ${SQUID_LOG_DIR} && \
    chmod -R 755 ${SQUID_LOG_DIR} && \
    chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_LOG_DIR}

# make cache dir
RUN mkdir -p ${SQUID_CACHE_DIR} && \
    chown -R ${SQUID_USER}:${SQUID_USER} ${SQUID_CACHE_DIR}


COPY squid.conf /etc/squid3/squid.conf
COPY start_squid.sh /usr/bin/

RUN chmod 777 /usr/bin/start_squid.sh

EXPOSE 3128/tcp

CMD bash -C '/usr/bin/start_squid.sh'
