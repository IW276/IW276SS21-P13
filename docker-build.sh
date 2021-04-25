#/bin/bash

# pass-through opencv from host so we don't have to deal with
# a time consuming compilation in the container
cp /etc/apt/sources.list.d/nvidia-l4t-apt-source.list .
cp /etc/apt/trusted.gpg.d/jetson-ota-public.asc .

docker image build -f Dockerfile -t p13-demo:1.0.0 .

# clean up after ourselves
rm nvidia-l4t-apt-source.list
rm jetson-ota-public.asc