%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define libggz_version %{version}

%define ggz_client_libs_version %{version}

Name:		ggz-gtk-client
Summary:	GGZ Client with GTK+ user interface
Version:	0.0.14.1
Release:	13
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/

# http://download.sf.net/ggz/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ggz-gtk-client-0.0.14.1-linkage_fix.diff

BuildRequires:	desktop-file-utils
BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(xft)
Requires:	ggz-client-libs = %{ggz_client_libs_version}
Suggests:	ggz-game-modules = %{version}

%description
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{libname}
Summary:	GGZ Library client with GTK+ user interface
Group:		Games/Other

%description -n	%{libname}
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{develname}
Summary:	Development files for GGZ Gaming Zone client with GTK+ user interface
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides: 	%{name}-devel = %{version}

%description -n	%{develname}
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains headers and other development files used for
building GGZ Gaming Zone GTK2+ client.

%prep
%setup -q
%patch0 -p0

%build
autoreconf -fis
%configure2_5x \
	--disable-static \
	--bindir=%{_gamesbindir} \
	--datadir="\${prefix}/share" \
	--with-libggz-libraries=%{_libdir} \
	--with-ggzcore-libraries=%{_libdir} \
	--with-ggzmod-libraries=%{_libdir} \

%make

%install
rm -rf %{buildroot}
%makeinstall_std


desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="GTK;Game" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang ggz-gtk

%files -f ggz-gtk.lang
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO README.GGZ QuickStart.GGZ
%{_gamesbindir}/ggz-gtk
%{_datadir}/applications/*
%{_datadir}/ggz/ggz-gtk-client/*
%{_datadir}/ggz/help/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libggz-gtk.so.%{major}*

%files -n %{develname}
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/lib*.so



%changelog
* Tue Dec 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.0.14.1-13
+ Revision: 738080
- added BR pkgconfig(xft)
- clean up spec
- disable static build
- removed .la files
- removed defattr, mkrel, BuildRoot, clean section
- removed old post/un scriptlets
- removed duplicate requires

  + Andrey Bondrov <abondrov@mandriva.org>
    - Rebuild to fix problems caused by Matthew Dawkins (.la issue)

* Sun Oct 16 2011 Andrey Bondrov <abondrov@mandriva.org> 0.0.14.1-11
+ Revision: 704875
- Rebuild to make libtool offer correct png version for linking

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-10
+ Revision: 664828
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-9mdv2011.0
+ Revision: 605451
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-8mdv2010.1
+ Revision: 521481
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.0.14.1-7mdv2010.0
+ Revision: 424875
- rebuild

* Sun Nov 09 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-6mdv2009.1
+ Revision: 301536
- fix linkage
- rebuilt against new libxcb

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.0.14.1-4mdv2009.0
+ Revision: 200645
- ggz-game-modules should be suggests

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.0.14.1-3mdv2009.0
+ Revision: 200635
- fix obsoletes

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 0.0.14.1-2mdv2009.0
+ Revision: 200629
- fix libname

* Tue Feb 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-1mdv2008.1
+ Revision: 175533
- New version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 16 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-2mdv2008.0
+ Revision: 52689
- drop debian menu
- drop gaim plugin


* Sat Feb 10 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-1mdv2007.0
+ Revision: 118746
- New version 0.0.14
- Import ggz-gtk-client

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-3mdv2007.0
- buildrequires desktop-file-utils
- fix devel package

* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-3mdv2007.0
- xdg menu
- fix x86_64 build

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-2mdk
- spec cleanup
- fix need of devel packages for main one

* Mon May 22 2006 Emmanuel Andry <eandry@mandriva.org> 0.0.13-1mdk
- New version
- mkrel
- drop patch 0 and 1
- libification

* Sat Nov 27 2004 Abel Cheung <deaddog@mandrake.org> 0.0.9-1mdk
- New version
- Drop P1 (UK server = default server)
- New P1: remove duplicated function declaration to fix build

* Wed Feb 11 2004 Abel Cheung <deaddog@deaddog.org> 0.0.8-1mdk
- New version
- Modify patch1 to add UK server to default server list

