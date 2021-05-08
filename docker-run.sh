#!/bin/sh

CONTAINER="asl-p13"

docker run $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && cat $DISPLAY && DISPLAY=:0.0 python3 demo.py"
