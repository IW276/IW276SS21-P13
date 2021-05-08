#!/bin/sh

CONTAINER="asl-p13"

docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
        $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && DISPLAY=:1.0 python3 demo.py"
