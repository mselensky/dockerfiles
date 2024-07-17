FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        gosu apt-utils
RUN apt-get install -y --no-install-recommends \
        openssh-server libopenmpi-dev openmpi-common openmpi-bin
RUN apt-get install python3 pip -y

# for good measure
RUN ln -s /usr/bin/python3 /usr/bin/python

# install mpi4py against openmpi inside container
# RUN MPICC="cc -shared" pip install --force-reinstall --no-cache-dir --no-binary=mpi4py mpi4py
RUN pip install --force-reinstall --no-cache-dir --no-binary=mpi4py mpi4py

# define /workdir and set entrypoint such that each container is run with a new user
# COPY entrypoint.sh /usr/local/bin/entrypoint.sh
# WORKDIR "/workdir"
# ENTRYPOINT ["sh", "/usr/local/bin/entrypoint.sh"]