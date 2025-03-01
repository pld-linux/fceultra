#
# Conditional build:
%bcond_with	qt6	# Qt 6 instead of Qt 5

Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	2.6.6
Release:	7
License:	GPL v2+
Group:		X11/Applications/Games
#Source0Download: https://fceux.com/web/download.html
# TODO: use named tarballs
#Source0:	https://github.com/TASEmulators/fceux/archive/v%{version}/fceux-%{version}.tar.gz
Source0:	https://github.com/TASEmulators/fceux/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	8e1aede624ebe26f0a936daba3b87328
Patch0:		%{name}-x265.patch
URL:		https://fceux.com/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	cmake >= 3.8
# libavcodec libavformat libavutil libswresample libswscale
BuildRequires:	ffmpeg-devel
BuildRequires:	libarchive-devel
BuildRequires:	libx264-devel
BuildRequires:	libx265-devel
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
# checked but not used
#BuildRequires:	xorg-lib-libX11-devel
#BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	zlib-devel
%if %{with qt6}
BuildRequires:	Qt6Core-devel >= 6.0
BuildRequires:	Qt6Gui-devel >= 6.0
BuildRequires:	Qt6Help-devel >= 6.0
BuildRequires:	Qt6OpenGL-devel >= 6.0
BuildRequires:	Qt6Widgets-devel >= 6.0
BuildRequires:	qt6-build >= 6.0
Requires:	Qt6Gui-platform-xcb-glx >= 5.11
%else
BuildRequires:	Qt5Core-devel >= 5.11
BuildRequires:	Qt5Gui-devel >= 5.11
BuildRequires:	Qt5Help-devel >= 5.11
BuildRequires:	Qt5OpenGL-devel >= 5.11
BuildRequires:	Qt5Widgets-devel >= 5.11
BuildRequires:	qt5-build >= 5.11
Requires:	Qt5Gui-platform-xcb-glx >= 5.11
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceux-%{version}
%patch -P 0 -p1

%build
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcxxflags}"
mkdir -p build
cd build
%cmake .. \
	-DQHELP=ON \
	%{?with_qt6:-DQT6=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man6
%{__mv} documentation/fceux.6 $RPM_BUILD_ROOT%{_mandir}/man6
%{__mv} documentation/fceux-net-server.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO-SDL changelog.txt readme.md documentation/*
%attr(755,root,root) %{_bindir}/fceux
%dir %{_datadir}/fceux
%dir %{_datadir}/fceux/luaScripts
%dir %{_datadir}/fceux/palettes
%dir %{_datadir}/fceux/tools
%{_datadir}/fceux/*.{dll,chm}
%{_datadir}/fceux/luaScripts/*
%{_datadir}/fceux/palettes/*
%{_datadir}/fceux/tools/*
%{_mandir}/man6/fceux-net-server.6*
%{_mandir}/man6/fceux.6*
%{_pixmapsdir}/fceux1.png
%{_desktopdir}/fceux.desktop
