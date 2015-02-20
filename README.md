Pantheon fork of systemd fedora git-pkg
=====================================

This is a fork of the fedora git-pkg for `systemd` with Pantheon
specific patches that are not available upstream yet.

Upstream: http://pkgs.fedoraproject.org/cgit/systemd.git

Adding a custom patch
---------------------

Edit the spec file, add a `PatchXXXX` statement. Use a number much
higher than what the upstream spec file uses, eg:

```
# kernel-install patch for grubby, drop if grubby is obsolete
Patch1000:      kernel-install-grubby.patch
 
# Pantheon backport of cgroup cache controller optimizations from systemd master branch (2013-11-21) -joe
Patch2000:      2000-cgroups-Cache-controller-masks-and-optimize-queues.patch
Patch2001:      2001-install-Assume-.wants-symlinks-have-the-same-name-as.patch

```

Pulling in Upstream changes
---------------------------

```
git clone git@github.com:pantheon-systems/systemd.git
cd systemd
git remote add upstream git://pkgs.fedoraproject.org/systemd.git
git fetch upstream

# merge in latest changes from upstream branch:
git rebase upstream/f20

# deal with any merge conflicts. hopefully none.
# then, you're ready to build a new rpm!
```

Building RPM
------------

NOTE: For fedora-20 We are currently adding '00' to the upstream fedora rpm version
 number so that we can avoid conflicts. Thus, before running the rpm build script you
 need to edit the `Release` line in `systemd.spec`. Eg:

    Release:        30%{?gitcommit:.git%{gitcommit}}%{?dist}
    Release:        3000%{?gitcommit:.git%{gitcommit}}%{?dist}

Do not commit this change to git, however, as it will cause version conflicts every
time we rebase on the `upstream/f20` branch. Also, do not worry about adding `pantheon1`
tag as this is done automatically by the rpm build script.


Building the RPM is done by running the `docker-build.sh` script which will take the following
actions:

1. pull down a docker image pre-populated with dev tools and rpm
  build tools.
2. execute `rpm-build.sh` inside the container
3. `rpmdev-bumpver` is called to append `.pantheon1` to the package version
  to identify this is a Pantheon-forked package.
3. on success, `.rpm`'s will be in an arch specific directory, eg: `x86_64`
