# Jupyter

This image contains Jupyter with R/Python cores. Jupyter Notebook will be 
executed automatically with following command.

```
docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged <image_name>
```

Jupyter Notebook is accessible via web browsers (i.e. firefox, chrome). Use the 
URL in messages displayed after the execution of the image.

Public dataset is automatically mounted on `/opt/dataset` once the image 
is successfully launched.
