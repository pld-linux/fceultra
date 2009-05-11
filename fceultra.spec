Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	2.1.0a
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/fceultra/fceux-%{version}.src.tar.bz2
# Source0-md5:	d48ed087e1cd5018ca8a4c9142130948
URL:		http://fceultra.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.0
BuildRequires:	SDL_gfx-devel >= 1.2.0
BuildRequires:	lua51-devel
BuildRequires:	scons
BuildRequires:	zenity
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceu
%{__sed} -i 's/lua5.1/lua51/g' SConstruct

%build
%scons
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/fceux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS changelog.txt TODO-PROJECT
%doc documentation
%attr(755,root,root) %{_bindir}/*
