#! /bin/bash
# RUN JUPYTER_NOTEBOOK
echo "RUN JUPYTER NOTEBOOK..."
${ANACONDA_BIN_HOME}/jupyter-notebook --ip 0.0.0.0 --no-browser --notebook-dir="${HOME}/jupyter-notebooks"
