#!/bin/sh

CONTAINER="asl-p13"

docker run --net=host --env="DISPLAY" \
        $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && DISPLAY=:1.0 python3 datareadandshow.py"
