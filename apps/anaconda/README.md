# Anaconda

This image contains Anaconda3 4.3.1. Anaconda is installed at
`/home/syndicate/anaconda3`.

> Anaconda is the leading open data science platform powered by Python. The open 
> source version of Anaconda is a high performance distribution of Python and R 
> and includes over 100 of the most popular Python, R and Scala packages for data 
> science. Additionally, you'll have access to over 720 packages that can easily 
> be installed with conda, our renowned package, dependency and environment 
> manager, that is included in Anaconda.

From (https://www.continuum.io/)[https://www.continuum.io/]

To exectue the image, use following command.
```
docker run -ti --privileged <image_name>
```

Public dataset is automatically mounted on `/opt/dataset` once the image 
is successfully launched.
