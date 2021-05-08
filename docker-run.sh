#!/bin/sh

CONTAINER="asl-p13"

docker run -it -d \
           --net=host \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --volume="/etc/machine-id:/etc/machine-id" \
           $CONTAINER /bin/bash -c "cd IW276SS21-P13/src && python3 datareadandshow.py"
export containerId=$(docker ps -l -q)

sudo xhost +local:`sudo docker inspect --format='{{ .Config.Hostname }}' $containerId`
sudo docker start $containerId
