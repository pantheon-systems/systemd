%global git_date    20100610
%global git_version 2f198e
%global _bindir      /bin
%global _libdir      /lib

Name:            systemd  
Url:             http://www.freedesktop.org/wiki/Software/systemd  
Version:         0
Release:         0.3.%{git_date}git%{git_version}%{?dist} 
License:         GPLv2+  
Group:           System Environment/Base
Summary:         A System and Session Manager  
BuildRequires:   libudev-devel  
BuildRequires:   libcap-devel  
BuildRequires:   libcgroup-devel libcgroup libxslt docbook-style-xsl
BuildRequires:   dbus-glib-devel vala pkgconfig gtk2-devel  
BuildRequires:   automake autoconf

# git clone git://anongit.freedesktop.org/systemd 
# cd systemd;
# git-archive --format=tar --prefix={name} {git_version} | xz  > systemd-{version}.{git_date}git{git_version}.tar.xz

Source0:         %{name}-%{version}.%{git_date}git%{git_version}.tar.xz
#Source0:        http://www.freedesktop.org/FIXME/%{name}-%{version}.tar.bz2  

  
%description 
systemd is a system and session manager for Linux, compatible with SysV and 
LSB init scripts. systemd provides aggressive parallelization capabilities, 
uses socket and D-Bus activation for starting services, offers on-demand 
starting of daemons, keeps track of processes using Linux cgroups, supports
snapshotting and restoring of the system state, maintains mount and automount 
points and implements an elaborate transactional dependency-based service 
control logic. It can work as a drop-in replacement for sysvinit.


%prep  
%setup -q -n %{name}
./bootstrap.sh
  
%build 
 
export V=1  
%configure --sbindir=/sbin  --libexecdir=%{_prefix}/libexec --with-rootdir=  --with-distro=fedora CFLAGS="%{optflags}"  

make %{?_smp_mflags}
  
%install  

# workaround for lack of init.d directory
mkdir -p %{buildroot}/%{_sysconfdir}/init.d

make DESTDIR=%{buildroot} install 


%files  
%defattr(-,root,root,-)  
%dir %{_sysconfdir}/systemd  
%{_sysconfdir}/systemd/*  
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.systemd1.conf  
%{_sysconfdir}/xdg/systemd/session  
%{_sysconfdir}/init.d/reboot
%{_datadir}/dbus-1/interfaces/org.freedesktop.systemd1.*.xml  
/lib/udev/rules.d/*.rules  
%{_bindir}/systemd  
%{_bindir}/systemctl 
%{_bindir}/systemadm  
%{_mandir}/man?/*.*
%{_libdir}/systemd
%{_datadir}/systemd/
%{_datadir}/dbus-1/services/org.freedesktop.systemd1.service
%{_datadir}/dbus-1/system-services/org.freedesktop.systemd1.service

  
%changelog
* Thu Jun 11 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.3.20100610git2f198e
- More minor fixes as per review

* Thu Jun 10 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.2.20100610git2f198e
- Spec improvements from David Hollis

* Wed Jun 09 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.1.20090609git2f198e
- Address review comments
 
* Tue Jun 01 2010 Rahul Sundaram <sundaram@fedoraproject.org> - 0-0.0.git2010-06-02
- Initial spec (adopted from Kay Sievers)

