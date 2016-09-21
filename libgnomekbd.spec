Summary:	A keyboard configuration library
Summary(pl.UTF-8):	Biblioteka do konfiguracji klawiatury
Name:		libgnomekbd
Version:	3.22.0.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomekbd/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	900ebf339d252c07d20f03e158399319
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	libxklavier >= 5.2
Conflicts:	control-center < 1:2.17.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to keyboard
configuration.

%description -l pl.UTF-8
Pakiet libgnomekbd zawiera bibliotekę GNOME zarządzającą konfiguracją
klawiatury i oferującą różne widgety związane z konfiguracją
klawiatury.

%package devel
Summary:	Header files for libgnomekbd
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgnomekbd
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0.0
Requires:	libxklavier-devel >= 5.2

%description devel
Header files for libgnomekbd.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgnomekbd.

%package static
Summary:	Static libgnomekbd library
Summary(pl.UTF-8):	Statyczna biblioteka libgnomekbd
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgnomekbd library.

%description static -l pl.UTF-8
Statyczna biblioteka libgnomekbd.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gkbd-keyboard-display
%attr(755,root,root) %{_libdir}/libgnomekbd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomekbd.so.8
%attr(755,root,root) %{_libdir}/libgnomekbdui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomekbdui.so.8
%{_desktopdir}/gkbd-keyboard-display.desktop
%{_datadir}/GConf/gsettings/libgnomekbd.convert
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/libgnomekbd
%{_libdir}/girepository-1.0/Gkbd-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomekbd.so
%attr(755,root,root) %{_libdir}/libgnomekbdui.so
%{_includedir}/libgnomekbd
%{_pkgconfigdir}/libgnomekbd.pc
%{_pkgconfigdir}/libgnomekbdui.pc
%{_datadir}/gir-1.0/Gkbd-3.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomekbd.a
%{_libdir}/libgnomekbdui.a
