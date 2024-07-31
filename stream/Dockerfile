FROM ubuntu:22.04

ARG DEBIAN_NONINTERACTIVE=true

RUN apt-get update -y && apt-get install wget build-essential ca-certificates -y

RUN wget https://www.cs.virginia.edu/stream/FTP/Code/stream.c 

RUN gcc stream.c \
  -DSTREAM_ARRAY_SIZE=2080000000 \
  -mcmodel=medium \
  -O3 \
  -fopenmp \
  -o /usr/bin/stream

