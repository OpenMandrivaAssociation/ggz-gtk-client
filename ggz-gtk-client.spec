%define major	1
%define libname %mklibname ggz-gtk %{major}
%define devname %mklibname -d ggz-gtk

Name:		ggz-gtk-client
Summary:	GGZ Client with GTK+ user interface
Version:	0.0.14.1
Release:	16
License:	GPLv2
Group:		Games/Other
Url:		http://ggzgamingzone.org/
# http://download.sf.net/ggz/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		ggz-gtk-client-0.0.14.1-linkage_fix.diff

BuildRequires:	desktop-file-utils
BuildRequires:	libggz-devel
BuildRequires:	ggz-client-libs-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(xft)
Requires:	ggz-client-libs
Suggests:	ggz-game-modules = %{version}

%description
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{libname}
Summary:	GGZ Library client with GTK+ user interface
Group:		Games/Other
Obsoletes:	%{_lib}ggz-gtk-client1 < 0.0.14.1-14

%description -n	%{libname}
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{devname}
Summary:	Development files for GGZ Gaming Zone client with GTK+ user interface
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides: 	%{name}-devel = %{version}
Obsoletes:	%{_lib}ggz-gtk-client-devel < 0.0.14.1-14

%description -n	%{devname}
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
%makeinstall_std

desktop-file-install --vendor="" \
	--remove-category="Application" \
	--remove-key="Encoding" \
	--add-category="GTK;Game" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

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

%files -n %{devname}
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/libggz-gtk.so

