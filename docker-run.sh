#!/bin/sh

export DISPLAY=:1

CONTAINER="asl-p13"

docker run -v /tmp/.X11-unix:/tmp/.X11-unix \
           --net=host \
           -e DISPLAY=$DISPLAY \
           $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 demo.py --datasets_path $1"

echo "Resulting images can be found in $1pipeline-results"

