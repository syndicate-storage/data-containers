# Anaconda
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-container-base
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

##############################################
# Setup Anaconda and R
##############################################
USER root
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends \
    wget make \
    fonts-dejavu gfortran gcc libxrender1 inkscape && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt /var/lib/cache /var/lib/log

USER $USER
ENV ANACONDA_HOME /home/$USER/anaconda3
ENV ANACONDA_BIN_HOME $ANACONDA_HOME/bin

RUN wget https://repo.continuum.io/archive/Anaconda3-4.3.1-Linux-x86_64.sh && \
    bash ./Anaconda3-4.3.1-Linux-x86_64.sh -b && \
    rm Anaconda3-4.3.1-Linux-x86_64.sh

USER $USER
    
RUN $ANACONDA_BIN_HOME/conda config --add channels r && \
    $ANACONDA_BIN_HOME/conda install --quiet --yes \
        'r-base=3.3.2' \
        'r-irkernel=0.7*' \
        'r-plyr=1.8*' \
        'r-devtools=1.12*' \
        'r-tidyverse=1.0*' \
        'r-shiny=0.14*' \
        'r-rmarkdown=1.2*' \
        'r-forecast=7.3*' \
        'r-rsqlite=1.1*' \
        'r-reshape2=1.4*' \
        'r-nycflights13=0.2*' \
        'r-caret=6.0*' \
        'r-rcurl=1.95*' \
        'r-crayon=1.3*' \
        'r-randomforest=4.6*' && \
    $ANACONDA_BIN_HOME/conda clean -tipsy

ENV PATH $PATH:$ANACONDA_BIN_HOME

USER root
COPY README.md $HOME/
RUN chown $USER:$USER $HOME/README.md
USER $USER
