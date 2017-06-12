# Mash
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-base
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

##############################################
# Setup Mash
##############################################
USER root
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends \
    wget unzip build-essential autoconf capnproto libcapnp-dev libcapnp-0.4.0 \
    libgsl0ldbl libgsl0-dev gsl-bin zlib1g-dev zlib1g && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt /var/lib/cache /var/lib/log

USER $USER
RUN wget -O mash.zip https://github.com/marbl/Mash/archive/master.zip && \
    unzip mash.zip && \
    rm mash.zip && \
    mv Mash-master mash

WORKDIR mash
RUN ./bootstrap.sh
RUN ./configure --prefix=/usr --with-capnp=/usr && \
    sed -i 's/\/usr\/lib\/libcapnp.a/\/usr\/lib\/x86_64-linux-gnu\/libcapnp.a/' Makefile && \
    sed -i 's/\/usr\/lib\/libkj.a/\/usr\/lib\/x86_64-linux-gnu\/libkj.a/' Makefile && \
    make

USER root
RUN make install
WORKDIR $HOME

RUN rm -rf mash

COPY README.md $HOME/
RUN chown $USER:$USER $HOME/README.md
USER $USER
