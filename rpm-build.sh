#!/bin/sh
#
# NOTE: this script is not intended to be called directly, although
#       given the proper build environment it should work.
#
#       Instead, please use `docker-build.sh` which will run this script
#       inside a docker container to ensure a predictable build environment.
#

spec_file='systemd.spec'

set -ex

yum -y -d1 install fedpkg
# fedpkg knows how to grab the tarballs needed for the build
fedpkg sources

# download and install all RPMs listed as BuildRequires
yum-builddep -y ${spec_file}

# bump version by adding '.pantheon1' to the rpm release
cp -f ${spec_file} ${spec_file}.orig
rpmdev-bumpspec --string pantheon ${spec_file}

# build it!!!!
#rpmbuild -ba ${spec_file}
fedpkg local

# reset ${spec_file}'s Release string by restoring the backup we made
cp -f ${spec_file}.orig ${spec_file}
