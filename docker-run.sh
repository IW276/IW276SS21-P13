#!/bin/sh

CONTAINER="asl-p13"

docker run -it -v $1:/datasets -v $2:/pipeline_results \
        $CONTAINER /bin/bash -c \
        "cd IW276SS21-P13/src && python3 demo.py --datasets_path /datasets/ --pipeline_results /pipeline_results/"

echo "Resulting images can be found in $2"
