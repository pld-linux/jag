#
# TODO: fix text display in the game
#
Summary:	2d arcade-puzzle game like KDiamonds
Summary(pl.UTF-8):	Logiczno-zręcznościowa gra podobna do KDiamonds
Name:		jag
Version:	0.3.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://jag.xlabsoft.com/files/%{name}-%{version}-src.zip
# Source0-md5:	78a408629ca9858dc8279d9c124386f7
Patch0:		%{name}-paths.patch
URL:		http://jag.xlabsoft.com
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtXml-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JAG is an arcade-puzzle 2D game similar to KDiamonds, Cradle of Rome,
Big Kahuna Reef etc. The aim of JAG is to break all of the target
pieces on each level, and to do this before the time runs out.

%description -l pl.UTF-8
JAG jest logiczno-zręcznościową grą podobną do KDiamonds, Cradle of
Rome, Big Kahuna Reef itp. Celem gry jest zniszczenie wszystkich
elementów na danym poziomie oraz zmieszczenie się w wyznaczonych
granicach czasu.

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1

# change dos formatting to unix one
%{__sed} -i -e 's,\r$,,' editor/editor.pro Game.pro main.cpp

%build
qmake-qt4
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcppflags} %{rpmcxxflags}" \
	LFLAGS="%{rpmcxxflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/jag
%{_datadir}/games/%{name}
