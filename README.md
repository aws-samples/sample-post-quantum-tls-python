# Post Quantum Python

This repository provides a Dockerfile configuring a container that supports
Post Quantum TLS provided in CPython. All PQ capabilities are derived from
public packages with no need to build anything from source.

This sample accompanies AWS Security blog ["Post Quantum TLS in Python"][1].

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
Crypto library: OpenSSL 3.5.0 8 Apr 2025
Testing ssl socket... ok
Testing requests... ok
Testing boto3... ok
Testing AWS CLI... ok
```

[1]: https://aws.amazon.com/blogs/security/post-quantum-tls-in-python
