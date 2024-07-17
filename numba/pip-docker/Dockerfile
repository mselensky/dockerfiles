FROM nvidia/cuda:12.4.0-devel-ubuntu22.04
ARG DEBIAN_FRONTEND=noninteractive

# install python
RUN apt-get update && apt-get install \
  libssl-dev \
  python3-dev \
  pip \
  --no-install-recommends -y

# for good measure
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN python -m pip install \
  numpy pandas numba scipy matplotlib 

