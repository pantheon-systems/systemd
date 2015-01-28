#!/bin/sh

CURRENT_DIR="$(dirname "$(readlink -f $0)")"

build_image=quay.io/getpantheon/rpmbuild-fedora-20

docker pull $build_image
docker run --rm \
    -w /root/rpmbuild/src \
    -v $CURRENT_DIR:/root/rpmbuild/src \
    $build_image \
    "/root/rpmbuild/src/rpm-build.sh"
