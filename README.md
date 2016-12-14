## Synopsis

Just a simple flask web front-end to [stress](http://people.seas.harvard.edu/~apw/stress/) for testing purposes


## Example HTTP requests 
Run with basic defaults
```
curl http://myhost/run
```
Run with 2 cpu workers and 4 vm workers with a 10 minute timeout
```
curl http://myhost/run?cpu=2&vm=4&timeout=10m
```

## Motivation

It is often the case where you need to test if basic host-based monitoring is set up properly on your containers or hosts. This small wrapper around stress allows us to simulate heavy load on CPU/Memory/Disk/IO in order to trigger alerts for the host it is ran on. A quick and easy way to test and ensure monitoring has been properly set up.


## Installation

see sample Dockerfile

Build the docker image and run
```
docker build -t stress .
docker run -d --name stress -p 8000:8000 --restart=always stress
```

Test using curl
```
curl http://127.0.0.1:8000/run?cpu=2&vm=4&timeout=10m
```


## References

stress - <http://people.seas.harvard.edu/~apw/stress/> 


