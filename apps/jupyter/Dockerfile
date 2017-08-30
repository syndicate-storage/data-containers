# Jupyter
#
# VERSION	1.0

FROM	syndicatestorage/syndicate-anaconda
MAINTAINER	Illyoung Choi <iychoi@email.arizona.edu>

USER root

ADD start_jupyter_notebook.sh /usr/bin/
RUN chmod 777 /usr/bin/start_jupyter_notebook.sh && \
    chown $USER:$USER /usr/bin/start_jupyter_notebook.sh

ENV JUPYTER_NOTEBOOK_HOME /opt/jupyter-notebooks

ADD jupyter-notebooks $JUPYTER_NOTEBOOK_HOME
RUN chown $USER:$USER $JUPYTER_NOTEBOOK_HOME


##############################################
# Setup R packages
##############################################
ADD Rprofile $HOME/.Rprofile
ADD install_r_packages.r $HOME/
RUN chmod 777 $HOME/install_r_packages.r

USER $USER
RUN $HOME/install_r_packages.r && \
    rm $HOME/install_r_packages.r

CMD bash -C '/usr/bin/init_container.sh';'start_jupyter_notebook.sh'

USER root
COPY README.md $HOME/
RUN chown $USER:$USER $HOME/README.md
USER $USER
