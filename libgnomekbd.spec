Summary:	A keyboard configuration library
Summary(pl.UTF-8):	Biblioteka do konfiguracji klawiatury
Name:		libgnomekbd
Version:	2.24.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomekbd/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	43e4d090bc67a1984bebf551637783fd
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.24.0
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	/sbin/ldconfig
Requires(post,preun):	GConf2
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
Requires:	GConf2-devel >= 2.24.0
Requires:	dbus-glib-devel >= 0.73
Requires:	gtk+2-devel >= 2:2.14.0

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
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%gconf_schema_install desktop_gnome_peripherals_keyboard_xkb.schemas

%preun
%gconf_schema_uninstall desktop_gnome_peripherals_keyboard_xkb.schemas

%postun
/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/gkbd-indicator-plugins-capplet
%attr(755,root,root) %{_libdir}/libgnomekbd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomekbd.so.3
%attr(755,root,root) %{_libdir}/libgnomekbdui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomekbdui.so.3
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard_xkb.schemas
%{_desktopdir}/gkbd-indicator-plugins-capplet.desktop
%{_datadir}/libgnomekbd

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomekbd.so
%attr(755,root,root) %{_libdir}/libgnomekbdui.so
%{_includedir}/libgnomekbd
%{_libdir}/libgnomekbd.la
%{_libdir}/libgnomekbdui.la
%{_pkgconfigdir}/libgnomekbd.pc
%{_pkgconfigdir}/libgnomekbdui.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomekbd.a
%{_libdir}/libgnomekbdui.a
