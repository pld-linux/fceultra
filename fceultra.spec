#
# TODO: bcond for non-gtk gui (gfceux)
#
Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	2.1.4a
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/fceultra/fceux-%{version}.src.tar.bz2
# Source0-md5:	a1252a888cdc8b2c42ae031211f2fad6
URL:		http://fceultra.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.14
BuildRequires:	SDL_gfx-devel >= 1.2.14
BuildRequires:	scons
BuildRequires:	zenity
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceu%{version}

%build
%scons

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a bin/fceux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Authors.txt README-SDL TODO-PROJECT TODO-SDL changelog.txt documentation
%attr(755,root,root) %{_bindir}/fceux