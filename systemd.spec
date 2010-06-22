%global git_date    20100622
%global git_version a3723b

Name:           systemd
Url:            http://www.freedesktop.org/wiki/Software/systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Version:        0
Release:        0.5.%{git_date}git%{git_version}%{?dist}
License:        GPLv2+
Group:          System Environment/Base
Summary:        A System and Session Manager
BuildRequires:  libudev-devel
BuildRequires:  libcap-devel
BuildRequires:  libcgroup-devel
BuildRequires:  tcp_wrappers-devel
BuildRequires:  pam-devel
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl
BuildRequires:  dbus-glib-devel
BuildRequires:  vala
BuildRequires:  pkgconfig
BuildRequires:  gtk2-devel
BuildRequires:  automake
BuildRequires:  autoconf
Requires:       dbus
Requires:       udev
Requires:       pkgconfig
Requires:       initscripts

# git clone git://anongit.freedesktop.org/systemd
# cd systemd;
# git archive --format=tar --prefix=systemd/ {git_version} | xz  > systemd-{version}.{git_date}git{git_version}.tar.xz

Source0:        %{name}-%{version}.%{git_date}git%{git_version}.tar.xz
#Source0:       http://www.freedesktop.org/FIXME/%{name}-%{version}.tar.bz2

%description
systemd is a system and session manager for Linux, compatible with
SysV and LSB init scripts. systemd provides aggressive parallelization
capabilities, uses socket and D-Bus activation for starting services,
offers on-demand starting of daemons, keeps track of processes using
Linux cgroups, supports snapshotting and restoring of the system
state, maintains mount and automount points and implements an
elaborate transactional dependency-based service control logic. It can
work as a drop-in replacement for sysvinit.

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
Conflicts:      sysvinit
Conflicts:      upstart

%description sysvinit
Drop-in replacement for the System V init tools of systemd.

%package pam
Group:          System Environment/Base
Summary:        systemd PAM module
Conflicts:      %{name} < %{version}-%{release}
Conflicts:      %{name} > %{version}-%{release}

%description pam
PAM module for creating per-user and per-session control groups in the
systemd control group hierarchy.

%prep
%setup -q -n %{name}
./bootstrap.sh ac

%build
%configure --with-rootdir= --with-distro=fedora
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
find %{buildroot} \( -name '*.a' -o -name '*.la' \) -exec rm {} \;
mkdir -p %{buildroot}/sbin
ln -s /bin/systemd %{buildroot}/sbin/init
ln -s /bin/systemctl %{buildroot}/sbin/reboot
ln -s /bin/systemctl %{buildroot}/sbin/halt
ln -s /bin/systemctl %{buildroot}/sbin/poweroff
ln -s /bin/systemctl %{buildroot}/sbin/shutdown
ln -s /bin/systemctl %{buildroot}/sbin/telinit
ln -s /bin/systemctl %{buildroot}/sbin/runlevel
rmdir %{buildroot}/cgroup

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/systemd
%{_sysconfdir}/xdg/systemd
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf
%{_sysconfdir}/rc.d/init.d/reboot
/bin/systemd
/bin/systemctl
/bin/systemd-notify
%{_bindir}/systemd-install
/lib/systemd
/lib/udev/rules.d/*.rules
%{_mandir}/man?/*.*
%{_datadir}/systemd
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml
%{_datadir}/pkgconfig/systemd.pc
%{_docdir}/systemd

%files gtk
%defattr(-,root,root,-)
%{_bindir}/systemadm

%files sysvinit
%defattr(-,root,root,-)
/sbin/init
/sbin/reboot
/sbin/halt
/sbin/poweroff
/sbin/shutdown
/sbin/telinit
/sbin/runlevel

%files pam
%defattr(-,root,root,-)
/%{_lib}/security/pam_systemd.so

%changelog
* Mon Jun 14 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.4.20100614.git393024
- Pull the latest snapshot that fixes a segfault. Resolves rhbz#603231

* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments

* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)
