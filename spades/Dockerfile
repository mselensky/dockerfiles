FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

### Install Packages and Libraries ###

## Compilers and Fetchers
RUN apt-get update -y && apt-get install -y wget git ca-certificates libssl-dev
RUN apt-get install -y build-essential cmake pkg-config 

## Other Libraries
RUN apt-get install -y  libbz2-dev zlib1g-dev
RUN apt-get install -y llvm

# Python, pip
RUN apt-get install python3 python3-pip -y
RUN ln -s `which python3` /usr/bin/python

# SPAdes
RUN wget https://github.com/ablab/spades/releases/download/v4.0.0/SPAdes-4.0.0.tar.gz && \
  tar -xzf SPAdes-4.0.0.tar.gz && \
  cd SPAdes-4.0.0 && \
  PREFIX=/usr/local bash ./spades_compile.sh

### Final things
ENV PATH=/usr/local/bin:$PATH