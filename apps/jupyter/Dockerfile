# Jupyter
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-anaconda
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

USER root

ADD start_jupyter_notebook.sh /usr/bin/
RUN chmod 777 /usr/bin/start_jupyter_notebook.sh && \
    chown $USER:$USER /usr/bin/start_jupyter_notebook.sh

RUN mkdir ${HOME}/jupyter-notebooks && \
    chown $USER:$USER ${HOME}/jupyter-notebooks


##############################################
# Setup R packages
##############################################
ADD Rprofile $HOME/.Rprofile
ADD install_r_packages.r $HOME/
RUN chmod 777 $HOME/install_r_packages.r

USER $USER
RUN $HOME/install_r_packages.r && \
    rm $HOME/install_r_packages.r

CMD start_jupyter_notebook.sh
