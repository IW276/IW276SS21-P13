# Project-Template for IW276 Autonome Systeme Labor

This repository uses basics of automatic white balancing and exposure compensation. The goal is to produce a better 
image representation for a neuronal net for detecting pedestrians.
Use the docker image to transform your original images to images that got automatic white balancing and exposure 
compensation.

<p style="margin-left: 50%;">
  <img src="./gif/result.gif"  alt="Project samples"/>
</p>

> This work was done by Johannes Brecht, Sophia Zimmer, Lukas Seitz during the IW276 Autonome Systeme Labor at the Karlsruhe University of Applied Sciences (Hochschule Karlruhe - Technik und Wirtschaft) in SS 2021.

## Table of Contents

* [Requirements](#requirements)
* [Prerequisites](#prerequisites)
* [Running](#running)
* [Acknowledgments](#acknowledgments)

## Requirements

* Jetson Nano
* Jetpack 4.5.1
* Docker 19.03 (or above)
* Python 3.9.2 (or above)
* OpenCV 4.5.1.48
* Matplotlib

## Prerequisites

The demo aka image stream pipeline has been containerized with docker to provide a clean runtime environment.

1. Clone the repository

```
// https
git clone https://github.com/IW276/IW276SS21-P13.git

// ssh
git clone git@github.com:IW276/IW276SS21-P13.git
```

2. Move inside the directory

```
cd IW276SS21-P13
```

3. Enable the jetson_clocks (to increase install/execution performance)

```
sudo jetson_clocks
```

### Displaying the pipeline results

For displaying the pipeline results you have to connect via a vnc client or use the jetson nano with an attached
hardware display.

## Docker

Both, the building and execution is done by using docker.

### Build

For building the docker image you only have to execute following code in a command-line (you have to be in directory
IW276SS21-P13)

```
$ sudo bash docker-build.sh
```

### Uploading Image

For uploading the docker image to the GitHub docker registry use following commands:

```
sudo bash docker-build.sh
cat ~/TOKEN.txt | docker login https://docker.pkg.github.com -u <GITHUB_USERNAME> --password-stdin
docker tag <image-id> docker.pkg.github.com/iw276/iw276ss21-p13/asl-p13:<version>
docker push docker.pkg.github.com/iw276/iw276ss21-p13/asl-p13:<version>
```

GITHUB_USERNAME is your GitHub username and in the TOKEN.txt should be your personal GitHub access token. Place the
image id of the built docker image into the placeholder <image-id>. For <version> use 1.0 as final release version.

### Running

By running the docker image, your inserted images will be processed in the pipeline. You have to execute following
command:

```
$ sudo bash docker-run.sh /full-image-directory-path/ /full-result-directory-path/
```

Mind that **/full-image-directory-path/** is the full path to the directory with the images that should be processed
from the pipeline and **/full-result-directory-path/** is the full path to the directory where the results should be
dropped. Both directories must exist!

Example:

```
$ sudo bash docker-run.sh /home/p13/IW276SS21-P13/datasets/demo/originals/ /home/p13/IW276SS21-P13/datasets/demo/results
```

After the pipeline processed the images, they will be displayed. You can press any key to display the next images.

## Acknowledgments

This repo is based on

- [Group P6](https://github.com/IW276/IW276WS20-P6)
- [Group P12](https://github.com/IW276/IW276WS20-P12)
- [Docker Image for Nano](https://github.com/IntelRealSense/librealsense/issues/5275#issuecomment-555830996)

Thanks to the original authors for their work!

## Contact

Please email `mickael.cormier AT iosb.fraunhofer.de` for further questions.
