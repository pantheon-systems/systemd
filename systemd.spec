Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Version:        4
Release:        2%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Summary:        A System and Session Manager
BuildRequires:  libudev-devel >= 160
BuildRequires:  libcap-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  dbus-glib-devel
BuildRequires:  vala >= 0.9
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
Requires:       systemd-units = %{version}-%{release}
Requires:       dbus >= 1.3.2
Requires:       udev >= 160
Requires:       libudev >= 160
Requires:       initscripts
Requires:       selinux-policy >= 3.8.7
Source0:        http://www.freedesktop.org/software/systemd/%{name}-%{version}.tar.bz2

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

%package units
Group:          System Environment/Base
Summary:        Configuration files, directories and installation tool for systemd
Requires:       pkgconfig

%description units
Basic configuration files, directories and installation tool for the systemd
system and session manager.

%package gtk
Group:          System Environment/Base
Summary:        Graphical frontend for systemd
Requires:       %{name} = %{version}-%{release}

%description gtk
Graphical front-end for systemd.

%package sysvinit
Group:          System Environment/Base
Summary:        systemd System V init tools
Requires:       %{name} = %{version}-%{release}
Obsoletes:      SysVinit < 2.86-24, sysvinit < 2.86-24
Provides:       SysVinit = 2.86-24, sysvinit = 2.86-24
Obsoletes:      upstart < 0.6.5-6.fc14
Conflicts:      upstart-sysvinit

# For now, require upstart installed, so that people can rely that
# they can emergency boot into upstart with init=/sbin/upstart
Requires:       upstart >= 0.6.5-6.fc14

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%prep
%setup -q

%build
%configure --with-rootdir= --with-distro=fedora
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;

# Create SysV compatibility symlinks. systemctl/systemd are smart
# enough to detect in which way they are called.
mkdir -p %{buildroot}/sbin
ln -s ../bin/systemd %{buildroot}/sbin/init
ln -s ../bin/systemctl %{buildroot}/sbin/reboot
ln -s ../bin/systemctl %{buildroot}/sbin/halt
ln -s ../bin/systemctl %{buildroot}/sbin/poweroff
ln -s ../bin/systemctl %{buildroot}/sbin/shutdown
ln -s ../bin/systemctl %{buildroot}/sbin/telinit
ln -s ../bin/systemctl %{buildroot}/sbin/runlevel

# We create all wants links manually at installation time to make sure
# they are not owned and hence overriden by rpm after the used deleted
# them.
rm -r %{buildroot}/etc/systemd/system/*.target.wants

# And the default symlink we generate automatically based on inittab
rm %{buildroot}/etc/systemd/system/default.target

%clean
rm -rf $RPM_BUILD_ROOT

%post units
if [ $1 -eq 1 ] ; then
        # Try to read default runlevel from the old inittab if it exists
        runlevel=$(/bin/awk -F ':' '$3 == "initdefault" && $1 !~ "^#" { print $2 }' /etc/inittab 2> /dev/null)
        if [ -z "$runlevel" ] ; then
                target="/lib/systemd/system/graphical.target"
        else
                target="/etc/systemd/system/runlevel$runlevel.target"
        fi

        # And symlink what we found to the new-style default.target
        /bin/ln -sf "$target" /etc/systemd/system/default.target 2>&1 || :

        # Enable the services we install by default.
        /bin/systemctl enable \
                getty@.service \
                prefdm.service \
                getty.target \
                rc-local.service \
                remote-fs.target 2>&1 || :
fi

%preun units
if [ $1 -eq 0 ] ; then
        /bin/systemctl disable \
                getty@.service \
                prefdm.service \
                getty.target \
                rc-local.service \
                remote-fs.target 2>&1 || :

        /bin/rm -f /etc/systemd/system/default.target 2>&1 || :
fi

%postun units
if [ $1 -ge 1 ] ; then
        /bin/systemctl daemon-reload 2>&1 || :
fi

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%{_sysconfdir}/rc.d/init.d/reboot
%dir %{_sysconfdir}/systemd/session
%{_sysconfdir}/xdg/systemd
/bin/systemd
/bin/systemd-notify
/lib/systemd/systemd-*
/lib/udev/rules.d/*.rules
/%{_lib}/security/pam_systemd.so
%{_bindir}/systemd-cgls
%{_mandir}/man1/systemd.*
%{_mandir}/man1/systemd-notify.*
%{_mandir}/man1/systemd-cgls.*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man7/*
%{_mandir}/man8/pam_systemd.*
%{_datadir}/systemd
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_docdir}/systemd

# Joint ownership with libcgroup
%dir /cgroup

%files units
%defattr(-,root,root,-)
%dir %{_sysconfdir}/systemd
%dir %{_sysconfdir}/systemd/system
%config(noreplace) %{_sysconfdir}/systemd/system.conf
%config(noreplace) %{_sysconfdir}/systemd/system/ctrl-alt-del.target
%config(noreplace) %{_sysconfdir}/systemd/system/display-manager.service
%config(noreplace) %{_sysconfdir}/systemd/system/kbrequest.target
%config(noreplace) %{_sysconfdir}/systemd/system/runlevel2.target
%config(noreplace) %{_sysconfdir}/systemd/system/runlevel3.target
%config(noreplace) %{_sysconfdir}/systemd/system/runlevel4.target
%config(noreplace) %{_sysconfdir}/systemd/system/runlevel5.target
%dir /lib/systemd
/lib/systemd/system
/bin/systemctl
%{_mandir}/man1/systemctl.*
%{_datadir}/pkgconfig/systemd.pc
%{_docdir}/systemd/LICENSE

%files gtk
%defattr(-,root,root,-)
%{_bindir}/systemadm
%{_mandir}/man1/systemadm.*

%files sysvinit
%defattr(-,root,root,-)
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel
%{_mandir}/man1/init.*
%{_mandir}/man8/halt.*
%{_mandir}/man8/reboot.*
%{_mandir}/man8/shutdown.*
%{_mandir}/man8/poweroff.*
%{_mandir}/man8/telinit.*
%{_mandir}/man8/runlevel.*

%changelog
* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-2
- Use the right tarball

* Sat Jul 24 2010 Lennart Poettering <lpoetter@redhat.com> - 4-1
- New upstream release, and make default

* Tue Jul 13 2010 Lennart Poettering <lennart@poettering.net> - 3-3
- Used wrong tarball

* Tue Jul 13 2010 Lennart Poettering <lennart@poettering.net> - 3-2
- Own /cgroup jointly with libcgroup, since we don't dpend on it anymore

* Tue Jul 13 2010 Lennart Poettering <lpoetter@redhat.com> - 3-1
- New upstream release

* Fri Jul 9 2010 Lennart Poettering <lpoetter@redhat.com> - 2-0
- New upstream release

* Wed Jul 7 2010 Lennart Poettering <lpoetter@redhat.com> - 1-0
- First upstream release

* Tue Jun 29 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.7.20100629git4176e5
- New snapshot
- Split off -units package where other packages can depend on without pulling in the whole of systemd

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.6.20100622gita3723b
- Add missing libtool dependency.

* Tue Jun 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0-0.5.20100622gita3723b
- Update snapshot

* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
