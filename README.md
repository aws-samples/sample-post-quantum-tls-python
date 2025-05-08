# Post Quantum Python

This repository provides a Dockerfile configuring a container that supports
Post Quantum TLS provided in CPython. All PQ capabilities are derived from
public packages with no need to build anything from source.

This sample accompanies [AWS Blog "<TITLE>"][1]

## Usage

To build and run the container, providing a shell:

```
docker build . -t pq-tls-python
docker run --rm -it pq-tls-python
```

A `run.sh` script is provided to simplify this on POSIX systems:

```
$ ./run.sh test.sh
...
ok
ok
ok
```

[1]: TODO
