Summary:	FCE Ultra - Linux Nintendo Entertainment System emulator
Summary(pl.UTF-8):	FCE Ultra - linuksowy emulator systemu Nintendo
Name:		fceultra
Version:	0.98.12
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/fceultra/fceu-%{version}.src.tar.bz2
# Source0-md5:	0fd2175b1f929e8b4d456789c4d7fc2b
URL:		http://fceultra.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL >= 1.2.0
BuildRequires:	SDL_gfx-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FCE Ultra is a cross platform, NTSC and PAL Famicom/NES emulator.

%description -l pl.UTF-8
FCE Ultra to wieloplatformowy emulator konsoli Famicom/NES/Pegasus.

%prep
%setup -q -n fceu

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-opengl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%doc Documentation
%attr(755,root,root) %{_bindir}/*
