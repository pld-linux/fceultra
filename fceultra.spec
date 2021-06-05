#
# TODO: bcond for non-gtk gui (gfceux)
# TODO: bcond for gtk3 interface instead of qt
#
Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	2.3.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/fceultra/fceux-%{version}.src.tar.gz
# Source0-md5:	1d7588d6cd74fa6a0473e529a6f823d9
URL:		http://fceultra.sourceforge.net/
BuildRequires:	Mesa-libGLU-devel
BuildRequires:	Qt5Core-devel >= 5.11
BuildRequires:	Qt5Gui-devel >= 5.11
BuildRequires:	Qt5OpenGL-devel >= 5.11
BuildRequires:	Qt5Widgets-devel >= 5.11
BuildRequires:	SDL2 >= 2.0
BuildRequires:	cmake
BuildRequires:	lua51-devel
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
Requires:	Qt5Gui-platform-xcb-glx >= 5.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceux-%{version}

%build
mkdir -p build
%cmake --build=build \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man6/
%{__mv} documentation/fceux.6 $RPM_BUILD_ROOT%{_mandir}/man6/
%{__mv} documentation/fceux-net-server.6 $RPM_BUILD_ROOT%{_mandir}/man6/

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
