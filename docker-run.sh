#!/bin/sh

# 1. argument: path to a video directory on the host.
# 2. argument: filename of the video to be processed as found in the path specified by the first argument.
#
# Returns: the output video placed in the video directory specified above.

CONTAINER="p13-demo:1.0.0"

docker run --runtime nvidia -v $1:/videos $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 demo.py $2"

echo "Resulting video can be found in $1"