#
# TODO: bcond for non-gtk gui (gfceux)
#
Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	2.2.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/fceultra/fceux-%{version}.src.tar.gz
# Source0-md5:	696d0186afb17f3b70d4aa9e9f5cf1d1
Patch0:		lua51.patch
Patch1:		format-security.patch
URL:		http://fceultra.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.14
BuildRequires:	SDL_gfx-devel >= 1.2.14
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
BuildRequires:	scons
BuildRequires:	zenity
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceux-%{version}
%patch0 -p1
%patch1 -p1

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
LDFLAGS="%{rpmldflags}" \
LIBS="-ldl" \
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a bin/fceux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors README-SDL TODO-SDL changelog.txt documentation
%attr(755,root,root) %{_bindir}/fceux
