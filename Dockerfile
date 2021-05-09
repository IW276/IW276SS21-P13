FROM nvcr.io/nvidia/l4t-pytorch:r32.5.0-pth1.7-py3
RUN echo "Build our Container based on L4T Pytorch"
RUN nvcc --version

COPY requirements.txt requirements.txt
COPY nvidia-l4t-apt-source.list /etc/apt/sources.list.d/nvidia-l4t-apt-source.list
COPY jetson-ota-public.asc /etc/apt/trusted.gpg.d/jetson-ota-public.asc

#Install all dependencies of the project
RUN apt-get update && \
        apt-get install -y libopencv-python && \
        apt-get install -y \
        python3-pip \
        build-essential \
        cmake

RUN pip3 install scikit-build

RUN git clone https://github.com/IW276/IW276SS21-P13.git && \
    cd IW276SS21-P13 && \
#    git checkout --track origin/master &&\
    chmod +x src/datareadandshow.py \
