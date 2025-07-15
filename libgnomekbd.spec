Summary:	A keyboard configuration library
Summary(pl.UTF-8):	Biblioteka do konfiguracji klawiatury
Name:		libgnomekbd
Version:	3.28.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/libgnomekbd/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	fe1c8072cea247d1e24e35dc13e4d67c
URL:		https://www.gnome.org/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.593
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
Requires(post,postun):	/sbin/ldconfig
Requires:	glib2 >= 1:2.44
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

%{__sed} -i -e '/^po\/Makefile\.in$/d' configure.ac

%build
# as of 3.28.0 meson support is incomplete (broken libraries soname, gir files not installed)
%if 1
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-static
%{__make}
%else
%meson

%meson_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if 1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%else
%meson_install
%endif

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
%{_libdir}/girepository-1.0/Gkbd-3.0.typelib
%{_datadir}/GConf/gsettings/libgnomekbd.convert
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd*.gschema.xml
%{_datadir}/libgnomekbd
%{_desktopdir}/gkbd-keyboard-display.desktop

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
