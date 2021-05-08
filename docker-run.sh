#!/bin/sh

CONTAINER="asl-p13"

docker run --net=host -v /tmp/.X11-unix:/tmp/.X11-unix \
           -e DISPLAY=$DISPLAY \
           -v="~/.Xauthority" \
           $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 datareadandshow.py"
export containerId=$(docker ps -l -q)

sudo xhost +local:`sudo docker inspect --format='{{ .Config.Hostname }}' $containerId`
sudo docker start $containerId
