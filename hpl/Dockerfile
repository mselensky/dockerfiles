FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

# required libraries
RUN apt-get update && apt-get install \
  wget \
  build-essential \
  libopenmpi-dev \
  --no-install-recommends -y

# download and unzip hpl v.2.3 in /hpl-2.3
# install instructions: https://www.netlib.org/benchmark/hpl/software.html
WORKDIR /
RUN wget https://www.netlib.org/benchmark/hpl/hpl-2.3.tar.gz --no-check-certificate
RUN gunzip hpl-2.3.tar.gz && tar -xvf hpl-2.3.tar

# define Makefile in top hpl directory (starting with this example for now)
WORKDIR /hpl-2.3
ARG arch=Linux_Intel64
RUN cp setup/Make.$arch .
RUN sed -iORG "s/openmp/qopenmp/"  Make.$arch
RUN make arch=$arch
