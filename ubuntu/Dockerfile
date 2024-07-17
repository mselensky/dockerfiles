FROM ubuntu:24.04

ENV INTEL_KEY_URL=https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
RUN curl -O $INTEL_KEY_URL | gpg --dearmor | tee /usr/share/keyrings/oneapi-archive-keyring.gpg

RUN echo "deb [signed-by=/usr/share/keyrings/oneapi-archive-keyring.gpg] https://apt.repos.intel.com/oneapi all main" | tee /etc/apt/sources.list.d/oneAPI.list

RUN apt-get update && apt-get install ca-certificates -y
RUN update-ca-certificates
RUN apt-get update && apt-get install intel-oneapi-runtime-compilers -y

RUN apt-get install gcc -y