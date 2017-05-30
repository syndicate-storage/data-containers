# POV (Pacific Oceans Virome)
Containerized POV dataset

Run from source
---------------
```
make
```

Run from pre-built image
------------------------
```
docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged syndicatestorage/pov-base
```
