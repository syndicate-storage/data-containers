# Data-containers Datasets
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-base
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

ARG MS_URL
ARG USER_NAME
ARG VOLUME_NAME
ARG GATEWAY_NAME
ARG DATASET_NAME

ENV MS_URL $MS_URL
ENV USER_NAME $USER_NAME
ENV VOLUME_NAME $VOLUME_NAME
ENV GATEWAY_NAME $GATEWAY_NAME
ENV DATASET_NAME $DATASET_NAME

##############################################
# Copy Syndicate mount script and run
##############################################
USER root

RUN mkdir /opt/private
COPY cert/$USER_NAME.pkey /opt/private/
RUN chown $USER:$USER -R /opt/private/

USER $USER

CMD mount_syndicatefs.sh $MS_URL $USER_NAME $VOLUME_NAME $GATEWAY_NAME $DATASET_NAME
