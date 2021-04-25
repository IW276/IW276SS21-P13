#!/bin/sh

# 1. argument: path to a video directory on the host.
# 2. argument: filename of the video to be processed as found in the path specified by the first argument.
#
# Returns: the output video placed in the video directory specified above.

CONTAINER="p13-demo:1.0.0"

docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" \
        $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 demo.py"