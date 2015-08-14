Name:           kmenuedit
Version:        5.3.95
Release:        1%{?dist}
Summary:        KDE menu editor

License:        GPLv2+
URL:            https://projects.kde.org/projects/kde/workspace/kmenuedit

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
BuildRequires:  kf5-kinit-devel >= 5.10.0-3

BuildRequires:  desktop-file-utils

Requires:       kf5-filesystem
# libkdeinit5_*
%{?kf5_kinit_requires}

# when split out from kde-workspace-4.11.x
Conflicts:      kde-workspace < 4.11.15-3

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%find_lang kmenuedit5 --with-qt --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kmenuedit.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f kmenuedit5.lang
%doc COPYING COPYING.DOC
%{_bindir}/kmenuedit
%{_kf5_libdir}/libkdeinit5_kmenuedit.so
%{_datadir}/kmenuedit/
%{_datadir}/applications/org.kde.kmenuedit.desktop
%{_datadir}/icons/hicolor/*/apps/kmenuedit.*
%{_kf5_datadir}/kxmlgui5/kmenuedit/
%lang(ca) %{_docdir}/HTML/ca/kmenuedit/
%lang(de) %{_docdir}/HTML/de/kmenuedit/
%lang(en) %{_docdir}/HTML/en/kmenuedit/
%lang(it) %{_docdir}/HTML/it/kmenuedit/
%lang(nl) %{_docdir}/HTML/nl/kmenuedit/
%lang(pt_BR) %{_docdir}/HTML/pt_BR/kmenuedit/
%lang(sv) %{_docdir}/HTML/sv/kmenuedit/
%lang(uk) %{_docdir}/HTML/uk/kmenuedit/


%changelog
* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.1-3
- tighten Conflicts: kde-workspace versioning

* Tue Jun 02 2015 Rex Dieter <rdieter@fedoraproject.org> 5.3.1-2
- +%%{kf5_kinit_requires}, %lang'ify docs, .spec cosmetics

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Wed Apr 22 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.95-1
- Plasma 5.2.95

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Fri Feb 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-2
- Rebuild (GCC 5)

* Tue Feb 24 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.1-1
- Plasma 5.2.1

* Mon Jan 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- Plasma 5.2.0

* Tue Jan 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-2.beta
- add icon scriptlets

* Mon Jan 12 2015 Daniel Vrátil <dvratil@redhat.com> - 5.1.95-1.beta
- Plasma 5.1.95 Beta

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

* Tue Aug 05 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-2
- Fix Obsoletes

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 5.0.0-1
- Plasma 5.0.0

* Sun May 18 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0.2-20140514git1b86b1a
- Rebuild due to build-id conflict with kf5-kded

* Wed May 14 2014 Daniel Vrátil <dvratil@redhat.com> - 4.96.0-1.20140514git1b86b1a
- Intial snapshot
