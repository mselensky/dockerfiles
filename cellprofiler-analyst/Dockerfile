FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install \
  libxxf86vm-dev \
  git \
  curl \
  openjdk-8-jre \
  openjdk-8-jdk \
  python3-dev \
  pkg-config \
  default-libmysqlclient-dev \
  build-essential \
  --no-install-recommends -y

RUN git clone https://github.com/CellProfiler/CellProfiler-Analyst.git
WORKDIR /CellProfiler-Analyst
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN apt-get install pip libpng-dev libjpeg-dev --no-install-recommends -y
RUN apt-get install libgtk2.0-dev libgtk-3-dev libglib2.0-dev --no-install-recommends -y
RUN apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev --no-install-recommends -y
RUN apt-get install libsdl1.2-dev --no-install-recommends -y
RUN apt-get install libgstreamer1.0-dev --no-install-recommends -y

ENV SDL_CONFIG=/usr/bin/sdl-config

# solve xlocale issue https://github.com/agracio/electron-edge-js/issues/16
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN python -m pip install numpy 
RUN python -m pip install python-javabridge
RUN python -m pip install .

# cleanup
#RUN rm -rf /CellProfiler-Analyst