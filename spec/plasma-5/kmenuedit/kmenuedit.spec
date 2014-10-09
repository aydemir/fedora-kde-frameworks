Name:           kmenuedit
Version:        5.1.0
Release:        1%{?dist}
Summary:        KDE menu editor

License:        GPLv2+
URL:            http://www.kde.org

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-sonnet-devel
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kdoctools-devel

Requires:       kf5-filesystem

# TODO: Remove once kmenuedit is split from kde-workspace
Obsoletes:      kde-workspace < 5.0.0-1

%description
%{summary}.

%prep
%setup -q

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}
%find_lang kmenuedit5 --with-qt --all-name

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f kmenuedit5.lang
%doc COPYING COPYING.DOC
%{_bindir}/kmenuedit
%{_kf5_libdir}/libkdeinit5_kmenuedit.so
%{_datadir}/kmenuedit
%{_datadir}/applications/kmenuedit.desktop
%{_datadir}/doc/HTML/en/kmenuedit
%{_datadir}/icons/hicolor/*/apps/kmenuedit.png


%changelog
* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Tue Aug 05 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-2
- Fix Obsoletes

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Sun May 18 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0.2-20140514git1b86b1a
- Rebuild due to build-id conflict with kf5-kded

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0-1.20140514git1b86b1a
- Intial snapshot
