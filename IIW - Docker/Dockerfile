FROM ubuntu:16.04

RUN apt-get update -y
RUN apt install -y build-essential
RUN apt install -y aptitude
RUN aptitude install libmagickwand-dev libmagickcore-dev imagemagick wget -y

WORKDIR /app
COPY . /app
WORKDIR /app/ImageMagick-7.0.9-8
RUN  ./configure
RUN  ["/bin/bash", "-c", "make"]
RUN  ["/bin/bash", "-c", "make install"]
WORKDIR /app
RUN LD_LIBRARY_PATH=/usr/local/lib
RUN export LD_LIBRARY_PATH
RUN ldconfig /usr/local/lib
RUN gcc -g -o server -O3 /app/detection.c /app/src/pattern/51Degrees.c /app/src/cityhash/city.c /app/src/threading.c /app/server.c /app/newHash.c /app/coda.c /app/imageToBlob.c `pkg-config --cflags --libs MagickWand` -lm -lpthread 
ENTRYPOINT ["/bin/sh", "-c", "./server 12345"]