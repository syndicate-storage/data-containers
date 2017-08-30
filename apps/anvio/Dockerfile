# Anvio
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-container-base
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

##############################################
# Setup Anvio
##############################################
USER root

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    apt-get install -y --allow-unauthenticated --no-install-recommends \
    build-essential wget python-dev python-pip python-numpy \
    cython libgsl0-dev libblas-dev liblapacke gfortran libopenblas-dev \
    liblapack-dev zlibc zlib1g-dev zlib1g sqlite libhdf5-serial-dev \
    libbz2-dev liblzma-dev && \
    apt-get clean autoclean && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt /var/lib/cache /var/lib/log

RUN pip install 'bottle>=0.12.9'
RUN pip install 'ete2>=2.3.10'
RUN pip install 'scipy>=0.17.1' 
RUN pip install 'scikit-learn>=0.17.1' 
RUN pip install 'django>=1.9.7'
RUN pip install 'h5py>=2.5.0'
RUN pip install 'cherrypy>=6.0.2'
RUN pip install 'requests>=2.10.0'

# prodigal
USER $USER
RUN wget https://github.com/hyattpd/Prodigal/archive/v2.6.2.tar.gz && \
    tar -zxvf v2.6.2.tar.gz

WORKDIR Prodigal-2.6.2
RUN make

USER root    
RUN cp prodigal /usr/bin/

WORKDIR $HOME
RUN rm -rf v2.6.2.tar.gz Prodigal-2.6.2

# hmmer
USER $USER
RUN wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2.tar.gz && \
    tar -zxvf hmmer-3.1b2.tar.gz 

WORKDIR hmmer-3.1b2
RUN ./configure && make

USER root
RUN make install

WORKDIR $HOME
RUN rm -rf hmmer-3.1b2 hmmer-3.1b2.tar.gz

# install anvio
RUN pip install anvio

COPY README.md $HOME/
RUN chown $USER:$USER $HOME/README.md
USER $USER
