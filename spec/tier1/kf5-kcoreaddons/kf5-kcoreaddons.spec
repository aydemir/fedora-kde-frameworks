#%define snapshot 20140205
%define framework kcoreaddons

Name:           kf5-%{framework}
Version:        4.99.0
Release:        2%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtCore

License:        GPLv2+
URL:            http://www.kde.org
# git archive --format=tar --prefix=%{framework}-%{version}/ \
#             --remote=git://anongit.kde.org/%{framework}.git master | \
# bzip2 -c > %{name}-%{version}-%{snapshot}git.tar.bz2
#Source0:        %{name}-%{version}-%{snapshot}git.tar.bz2
Source0:        http://download.kde.org/unstable/frameworks/4.99.0/%{framework}-4.99.0.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires:       kf5-filesystem

%description
KCoreAddons provides classes built on top of QtCore to perform various tasks
such as manipulating mime types, autosaving files, creating backup files,
generating random sequences, performing text manipulations such as macro
replacement, accessing user information and many more.

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
%find_lang kcoreaddons5_qt --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f kcoreaddons5_qt.lang
%doc COPYING.LIB README.md
%{_kf5_libdir}/libKF5CoreAddons.so.*
%{_kf5_datadir}/mime/packages/kde5.xml

%files devel
%{_kf5_includedir}/kcoreaddons_version.h
%{_kf5_includedir}/KCoreAddons/
%{_kf5_libdir}/libKF5CoreAddons.so
%{_kf5_libdir}/cmake/KF5CoreAddons
%{_kf5_archdatadir}/mkspecs/modules/qt_KCoreAddons.pri

%changelog
* Tue May 06 2014 Daniel Vrátil <dvratil@redhat.com>
- Rebuild against updated kf5-rpm-macros

* Mon May 05 2014 Daniel Vrátil <dvratil@redhat.com> - 4.99.0
- KDE Frameworks 4.99.0

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
