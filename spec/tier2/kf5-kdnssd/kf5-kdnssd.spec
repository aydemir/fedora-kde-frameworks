#%define snapshot 20140205
%define framework kdnssd

Name:           kf5-%{framework}
Version:        4.98.0
Release:        1.20140418git5559d457%{?dist}
Summary:        KDE Frameworks 5 Tier 2 integration module for DNS-SD services (Zeroconf)

License:        GPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-framework-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}-framework.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        kf5-kdnssd-5559d457.tar

BuildRequires:  avahi-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       nss-mdns
Requires:       kf5-filesystem

%description
KDE Frameworks 5 Tier 2 integration module for DNS-SD services (Zeroconf)

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5DNSSD.so.*

%files devel
%{_kf5_includedir}/KDNSSD
%{_kf5_libdir}/libKF5DNSSD.so
%{_kf5_libdir}/cmake/KF5DNSSD
%{_kf5_archdatadir}/mkspecs/modules/qt_KDNSSD.pri

%changelog
* Fri Apr 18 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140418git5559d457
- Update to git: 5559d457

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-relase snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
