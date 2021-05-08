#!/bin/sh

CONTAINER="asl-p13"

docker run $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && DISPLAY=:0.1 python3 demo.py"
