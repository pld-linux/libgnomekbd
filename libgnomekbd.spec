#
# TODO:
# - pl summary and description
#
Summary:	A keyboard configuration library
Name:		libgnomekbd
Version:	2.18.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomekbd/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	f176e026158f678144511fb343ec7269
URL:		http://www.gnome.org/
BuildRequires:	GConf2-devel >= 2.18.0.1
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.17.92
BuildRequires:	libtool
BuildRequires:	libxklavier-devel >= 3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Conflicts:	control-center < 1:2.17.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libgnomekbd package contains a GNOME library which manages
keyboard configuration and offers various widgets related to keyboard
configuration.

%package devel
Summary:	Header files for libgnomekbd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libgnomekbd.

%package static
Summary:	Static libgnomekbd library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgnomekbd library.

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
