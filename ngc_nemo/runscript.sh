#!/bin/bash

#### CUDA 12.4 compatible container for NeMo ####

# base image (cuda 12.4)
docker build . -t mjsel/ubuntu22.04:cuda12.4 --platform=linux/amd64 -f Dockerfile-from-ubuntu 

# nemo image bootstrapped from base
docker build . -t mjsel/ngc_nemo:24.05.01 --platform=linux/amd64 -f Dockerfile-nemo
