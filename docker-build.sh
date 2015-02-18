#!/bin/sh
# starts a docker container and kicks off rpm-build.sh inside of it

CURRENT_DIR="$(dirname "$(readlink -f $0)")"

build_image=quay.io/getpantheon/rpmbuild-fedora-20

docker pull $build_image
docker run --rm -it \
    -w /root/rpmbuild/src \
    -v $CURRENT_DIR:/root/rpmbuild/src \
    $build_image \
    "/root/rpmbuild/src/rpm-build.sh"
