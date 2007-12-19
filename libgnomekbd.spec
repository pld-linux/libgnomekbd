Summary:	A keyboard configuration library
Summary(pl.UTF-8):	Biblioteka do konfiguracji klawiatury
Name:		libgnomekbd
Version:	2.21.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgnomekbd/2.21/%{name}-%{version}.tar.bz2
# Source0-md5:	149a45d15f85dbfea7a59801e365bfe2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-popt.patch
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.19.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gtk+2-devel >= 2:2.10.14
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.19.1
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
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
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgnomekbd.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libgnomekbd.

%package static
Summary:	Static libgnomekbd library
Summary(pl.UTF-8):	Statyczna biblioteka libgnomekbd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgnomekbd library.

%description static -l pl.UTF-8
Statyczna biblioteka libgnomekbd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall desktop_gnome_peripherals_keyboard_xkb.schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/gkbd-indicator-plugins-capplet
%attr(755,root,root) %{_libdir}/libgnomekbd.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnomekbdui.so.*.*.*
%{_sysconfdir}/gconf/schemas/desktop_gnome_peripherals_keyboard_xkb.schemas
%{_desktopdir}/gkbd-indicator-plugins-capplet.desktop
%{_iconsdir}/hicolor/*/*/*.png
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
