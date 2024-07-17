FROM nvcr.io/nvidia/mlperf/mlperf-inference:mlpinf-v4.0-cuda12.2-cudnn8.9-x86_64-ubuntu20.04-public

# for good measure
RUN ln -s /usr/bin/python3 /usr/bin/python

#COPY training .

RUN apt-get update && apt-get install python3 python3.8-venv git wget curl libglu1-mesa-dev libglib2.0-0 -y

RUN python -m pip install ninja \
                yacs \
                cython \
                matplotlib \
                opencv-python \
                mlperf_compliance 
RUN TMPDIR=`pwd` python -m pip install torchvision \
                pycocotools

RUN python -m pip install tabulate

RUN python -m pip install --no-cache-dir https://github.com/mlperf/logging/archive/9ea0afa.zip


# install cm interface for MLPerf
RUN python3 -m venv cm
RUN chmod +x cm/bin/activate 
RUN ./cm/bin/activate && python3 -m pip install cmind


