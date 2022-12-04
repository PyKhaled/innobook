# Innobook

Simple Phonebook api

## Getting Started

As it simple we need to build the image and run it 


```bash
# build the docker image
$ docker build . -t innobook:latest
```

```bash 
# run docker container from the image we has build 
$ docker run --name ahmed_khaled_task -p 8000:8000 -d innobook:latest
```

### Running the tests

```bash
# to run test in local environment
$ python3 manage.py test
```
