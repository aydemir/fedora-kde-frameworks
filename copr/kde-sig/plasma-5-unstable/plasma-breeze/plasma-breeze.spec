%global         base_name   breeze

%global         build_kde4  1

Name:           plasma-breeze
Version:        5.4.90
Release:        2%{?dist}
Summary:        Artwork, styles and assets for the Breeze visual style for the Plasma Desktop

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/breeze

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/plasma/%{version}/%{base_name}-%{version}.tar.xz

BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:	kf5-kservice-devel
BuildRequires:  kf5-kcmutils-devel
BuildRequires:  kf5-plasma-devel

# kde4breeze
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kguiaddons-devel

# kstyle
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-frameworkintegration-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kdecoration-devel

BuildRequires:  libxcb-devel

BuildRequires:  gettext

# icon optimizations
BuildRequires: hardlink
# for optimizegraphics
BuildRequires: kde-dev-scripts
BuildRequires: time

Requires:       kf5-filesystem

Requires:       %{name}-common = %{version}-%{release}

%description
%{summary}.

%package        common
Summary:        Common files shared between KDE 4 and Plasma 5 versions of the Breeze style
BuildArch:      noarch
%description    common
%{summary}.

%package -n     breeze-cursor-theme
Summary:	Breeze cursor theme
BuildArch:	noarch
%description -n breeze-cursor-theme
%{summary}.

%if 0%{?build_kde4:1}
%package -n     kde-style-breeze
Summary:        KDE 4 version of Plasma 5 artwork, style and assets
BuildRequires:  kdelibs4-devel
BuildRequires:  libxcb-devel
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      plasma-breeze-kde4 < 5.1.95
Provides:       plasma-breeze-kde4%{?_isa} = %{version}-%{release}
%description -n kde-style-breeze
%{summary}.
%endif


%prep
%autosetup -n %{base_name}-%{version} -p1

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%if 0%{?build_kde4:1}
mkdir -p %{_target_platform}_kde4
pushd %{_target_platform}_kde4
%{cmake_kde4} -DUSE_KDE4=TRUE ..
popd

make %{?_smp_mflags} -C %{_target_platform}_kde4
%endif


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang breeze --with-qt --all-name

%if 0%{?build_kde4:1}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}_kde4
%endif

# icon optimizations
for theme in breeze_cursors Breeze_Snow; do
pushd %{buildroot}%{_datadir}/icons/${theme}
du -s  .
time optimizegraphics ||:
du -s .
/usr/sbin/hardlink -c -v %{buildroot}%{_datadir}/icons/${theme}
du -s .
popd
done


%post
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%files
%doc cursors/Breeze/README COPYING COPYING-ICONS
%{_kf5_qtplugindir}/org.kde.kdecoration2/breezedecoration.so
%{_kf5_qtplugindir}/styles/breeze.so
%{_kf5_datadir}/kstyle/themes/breeze.themerc
%{_kf5_qtplugindir}/kstyle_breeze_config.so
%{_kf5_datadir}/kconf_update/kde4breeze.upd
%{_kf5_libdir}/kconf_update_bin/kde4breeze
%{_kf5_qmldir}/QtQuick/Controls/Styles/Breeze
%{_bindir}/breeze-settings5
%{_datadir}/icons/hicolor/scalable/apps/breeze-settings.svgz
%{_kf5_datadir}/kservices5/breezedecorationconfig.desktop
%{_kf5_datadir}/kservices5/breezestyleconfig.desktop
%{_kf5_datadir}/kservices5/plasma-lookandfeel-org.kde.breezedark.desktop.desktop
%{_kf5_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/

%files common -f breeze.lang
%{_datadir}/color-schemes/*.colors
%{_datadir}/QtCurve/Breeze.qtcurve
%{_datadir}/wallpapers/Next

%if 0%{?build_kde4:1}
%files -n kde-style-breeze
%{_kde4_libdir}/kde4/plugins/styles/breeze.so
%{_kde4_libdir}/kde4/kstyle_breeze_config.so
%{_kde4_appsdir}/kstyle/themes/breeze.themerc
%endif

%post -n breeze-cursor-theme
touch --no-create %{_kf5_datadir}/icons/Breeze_Snow &> /dev/null || :
touch --no-create %{_kf5_datadir}/icons/breeze_cursors &> /dev/null || :

%posttrans -n breeze-cursor-theme
gtk-update-icon-cache %{_kf5_datadir}/icons/Breeze_Snow &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/breeze_cursors &> /dev/null || :

%postun -n breeze-cursor-theme
if [ $1 -eq 0 ] ; then
touch --no-create %{_kf5_datadir}/icons/Breeze_Snow &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/Breeze_Snow &> /dev/null || :
touch --no-create %{_kf5_datadir}/icons/breeze_cursors &> /dev/null || :
gtk-update-icon-cache %{_kf5_datadir}/icons/breeze_cursors &> /dev/null || :
fi

%files -n breeze-cursor-theme
%{_kf5_datadir}/icons/Breeze_Snow
%ghost %{_kf5_datadir}/icons/Breeze_Snow/index.theme
%{_kf5_datadir}/icons/breeze_cursors
%ghost %{_kf5_datadir}/icons/breeze_cursors/index.theme


%changelog
* Sun Nov 08 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.90-1
- Plasma 5.4.90

* Fri Nov 06 2015 Daniel Vrátil <dvraitl@fedoraproject.org> - 5.4.3-2
- tarball respin

* Thu Nov 05 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Plasma 5.4.3

* Tue Oct 13 2015 Jan Grulich <jgrulich@redhat.com> - 5.4.2-2
- Fix breeze-dark icons inheritance

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-1
- 5.4.2

* Wed Sep 16 2015 Rex Dieter <rdieter@fedoraproject.org> 5.4.1-2
- breeze-icon-theme: optimizegraphics,hardlink optimizations

* Wed Sep 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.1-1
- 5.4.1

* Fri Aug 21 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- Plasma 5.4.0

* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.95-1
- Plasma 5.2.95

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Tue Mar 10 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.2.1-3
- backport upstream fixes (mostly crashers)
- .spec cosmetics

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

* Mon Jan 05 2015 Jan Grulich <jgrulich@redhat.com> - 5.1.1-2
- better URL
  breeze-kde4 renamed to kde-style-breeze
  created breeze-icon-theme subpackage
  used make install instead of make_install macro

* Wed Dec 17 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.2-2
- Plasma 5.1.2

* Fri Nov 07 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.1-1
- Plasma 5.1.1

* Tue Oct 14 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0.1-1
- Plasma 5.1.0.1

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- Plasma 5.1.0

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.2-1
- Plasma 5.0.2

* Sun Aug 10 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.1-1
- Plasma 5.0.1

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.90.1-1.20140514git73a19ea
- Update to latest upstream

* Fri May 02 2014 Jan Grulich <jgrulich@redhat.com> 4.90.1-0.1.20140502git
- Initial version