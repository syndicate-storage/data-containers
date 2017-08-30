# Mash
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-container-base
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

USER root
COPY README.md $HOME/
RUN chown $USER:$USER $HOME/README.md
USER $USER
