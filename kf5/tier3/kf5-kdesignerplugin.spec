%define snapshot  20140109

Name:           kf5-kdesignerplugin
Version:        5.0.0
Release:        0.1.%{snapshot}git
Summary:        KDE Frameworks tier 3 integration module for QtDesigner

License:        GPLv2+
URL:            http://www.kde.org

# git archive --format=tar --prefix=%{name}-%{snapshot}/ \
#             --remote=git://anongit.kde.org/%{name}-framework.git master | \
# gzip -c > %{name}-framework-%{snapshot}.tar.gz
Source0:        %{name}-%{snapshot}.tar.gz

BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtwebkit-devel

BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  attica-qt5-devel

# optional requirements
BuildRequires:  kf5-kguiaddons-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kjs-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kservice-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kglobalaccel-devel
BuildRequires:  kf5-sonnet-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kbookmarks-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kplotting-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kdewebkit-devel
BuildRequires:  kf5-kjobwidgets-devel



%description
KDE Frameworks tier 3 integration module for QtDesigner


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

make %{?_smp_mflags} DESTDIR=%{buildroot} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc COPYING.LIB README.md
%{_kf5_bindir}/kgendesignerplugin
%{_kf5_mandir}/man1/kgendesignerplugin.1
%{_kf5_libdir}/plugins/designer/*.so
%{_kf5_datadir}/kf5widgets/*

%files devel
%doc
%{_kf5_libdir}/cmake/KF5DesignerPlugin


%changelog
* Sat Jan  4 2014 Daniel Vrátil <dvratil@redhat.com>
- initial version
