#!/bin/sh

export DISPLAY=:1

CONTAINER="asl-p13"

docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
           $1:/datasets\
           --net=host \
           -e DISPLAY=$DISPLAY \
           $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 demo.py --datasets_path /datasets/"

echo "Resulting images can be found in $1/pipeline-results"
