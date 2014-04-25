#%define snapshot 20140207
%define framework kwindowsystem

Name:           kf5-%{framework}
Version:        4.98.0
Release:        1.20140425giteea0539f%{?dist}
Summary:        KDE Frameworks 5 Tier 1 integration module with classes for windows management

License:        GPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        kf5-kwindowsystem-eea0539f.tar

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  libX11-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  libXrender-devel

Requires:       kf5-filesystem

%description
KDE Frameworks tier 1 integration module that provides classes for managing and
working with windows


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
%{_kf5_libdir}/libKF5WindowSystem.so.*

%files devel
%{_kf5_includedir}/kwindowsystem_version.h
%{_kf5_includedir}/KWindowSystem
%{_kf5_libdir}/libKF5WindowSystem.so
%{_kf5_libdir}/cmake/KF5WindowSystem
%{_kf5_archdatadir}/mkspecs/modules/qt_KWindowSystem.pri


%changelog
* Fri Apr 25 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140425giteea0539f
- Update to git: eea0539f

* Tue Apr 22 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140422git93577187
- Update to git: 93577187

* Fri Apr 18 2014 dvratil <dvratil@redhat.com> - 4.98.0-20140418gite7df8dd1
- Update to git: e7df8dd1

* Mon Mar 31 2014 Jan Grulich <jgrulich@redhat.com> 4.98.0-1
- Update to KDE Frameworks 5 Beta 1 (4.98.0)

* Wed Mar 05 2014 Jan Grulich <jgrulich@redhat.com> 4.97.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.97.0)

* Wed Feb 12 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-1
- Update to KDE Frameworks 5 Alpha 1 (4.96.0)

* Wed Feb 05 2014 Daniel Vrátil <dvratil@redhat.com> 4.96.0-0.1.20140205git
- Update to pre-release snapshot of 4.96.0

* Thu Jan 09 2014 Daniel Vrátil <dvratil@redhat.com> 4.95.0-1
- Update to KDE Frameworks 5 TP1 (4.95.0)

* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
