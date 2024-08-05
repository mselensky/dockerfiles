FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu22.04


### Install Packages and Libraries ###

# python and pip
RUN apt-get update -y && apt-get install python3 python3-pip -y
RUN ln -s `which python3` /usr/bin/python
#RUN python -m ensurepip --upgrade

# other libraries
RUN apt-get install -y libsndfile1 ffmpeg 
RUN apt-get install -y wget git ca-certificates

# pytorch wheels for cuda 12.4
RUN python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# other packages
RUN python -m pip install Cython packaging
RUN python -m pip install numba
RUN python -m pip install "pybind11[global]"


### Install tools ###

# define number of cores to use for compiling
ARG BUILD_CORES=6

RUN mkdir -p /tools
WORKDIR /tools

# Tool: Apex
RUN git clone https://github.com/NVIDIA/apex
WORKDIR /tools/apex
# if pip >= 23.1 (ref: https://pip.pypa.io/en/stable/news/#v23-1) which supports multiple `--config-settings` with the same key... 
RUN pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global-option="--cuda_ext" ./

# Tool: OpenMPI
WORKDIR /tools/openmpi
RUN wget https://download.open-mpi.org/release/open-mpi/v5.0/openmpi-5.0.5.tar.bz2 
RUN tar -xf openmpi-5.0.5.tar.bz2
WORKDIR openmpi-5.0.5
RUN ./configure --prefix=/usr/local 2>&1 | tee config.out
RUN make -j $BUILD_CORES all 2>&1 | tee make.out
RUN make -j $BUILD_CORES install 2>&1 | tee make-install.out

# Tool: Transformer Engine
#Possibly need to upgrade Transformer Engine; skip for now
#WORKDIR /tools/
#RUN curl -O https://github.com/NVIDIA/Megatron-LM/archive/refs/tags/core_v0.7.0.tar.gz

# Tool: Megatron Core
ENV MEGATRON_VERSION=core_v0.7.0
WORKDIR /tools/megatron
RUN wget https://github.com/NVIDIA/Megatron-LM/archive/refs/tags/${MEGATRON_VERSION}.tar.gz
RUN tar -xzf ${MEGATRON_VERSION}.tar.gz 
RUN cd Megatron-LM-${MEGATRON_VERSION} && pip install .
RUN cd Megatron-LM-${MEGATRON_VERSION}/megatron/core/datasets && \
  make -j $BUILD_CORES


### App: NeMo ###
RUN python -m pip install nemo_toolkit['all']


### Final things ###
WORKDIR /workdir