#!/bin/sh

CONTAINER="asl-p13"

docker run --net=host -v /tmp/.X11-unix:/tmp/.X11-unix \
           -e DISPLAY=$DISPLAY \
           $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 datareadandshow.py"
