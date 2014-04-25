%global         framework modemmanagerqt
%global         git_commit d257bb2
Name:           kf5-%{framework}
Version:        5.0.90
Release:        1.20140425git4988794c%{?dist}
Summary:        A Tier 1 KDE Frameworks module wrapping ModemManager DBus API

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://projects.kde.org/projects/extragear/libs/libmm-qt

#Source0:        http://download.kde.org/unstable/modemmanager-qt/%{version}/src/%{name}-%{version}.tar.xz
# Package from git snapshots using releaseme scripts
Source0:        kf5-modemmanagerqt-4988794c.tar

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ModemManager-devel >= 1.0.0

Requires:       kf5-filesystem

%description
A Qt 5 library for ModemManager

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Qt 5 libraries and header files for developing applications that use ModemManager

%prep
%setup -qn kf5-%{framework}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README
%{_kf5_libdir}/libKF5ModemManagerQt.so.*

%files devel
%{_kf5_libdir}/libKF5ModemManagerQt.so
%{_kf5_libdir}/cmake/KF5ModemManagerQt
%{_kf5_includedir}/ModemManagerQt
%{_kf5_includedir}/modemmanagerqt_version.h
%{_kf5_archdatadir}/mkspecs/modules/qt_ModemManagerQt.pri

%changelog
* Fri Apr 25 2014 dvratil <dvratil@redhat.com> - 5.0.90-20140425git4988794c
- Update to git: 4988794c

* Fri Apr 18 2014 dvratil <dvratil@redhat.com> - 5.0.90-20140418git4ff37cb3
- Update to git: 4ff37cb3

* Fri Apr 18 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.90-1.20140418gitd257bb2
- Upgrade libmm-qt to Tier 1 KDE Framework kf5-modemmanagerqt

* Thu Apr 03 2014 Daniel Vrátil <dvratil@redhat.com> - 1:1.0.1-1.20140403gitd257bb2
- Qt 5 fork of libmm-qt
