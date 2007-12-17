%define name	ggz-gtk-client
%define version 0.0.14
%define release %mkrel 2


%define libname %mklibname %{name}

%define libggz_version %{version}

%define ggz_client_libs_version %{version}

Name:		%{name}
Summary:	GGZ Client with GTK+ user interface
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/

# http://download.sf.net/ggz/
Source:		%{name}-%{version}.tar.bz2

BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
BuildRequires:	gtk+2-devel desktop-file-utils
Requires:	libggz = %{libggz_version}
Requires:	ggz-client-libs = %{ggz_client_libs_version}
Requires:	ggz-game-modules = %{version}

%description
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{libname}
Summary:	GGZ Library client with GTK+ user interface
Group:		Games/Other
Provides:	%{libname} = %{version}

%description -n	%{libname}
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{libname}-devel
Summary:	Development files for GGZ Gaming Zone client with GTK+ user interface
Group:		Development/Other
Requires:	%{libname} = %{version}
Requires:	libggz-devel = %{libggz_version}
Provides: 	%{libname}-devel

%description -n	%{libname}-devel
The GGZ client libraries are necessary for running and/or developing
GGZ Gaming Zone clients and games.

This package contains headers and other development files used for
building GGZ Gaming Zone GTK2+ client.

%prep
%setup -q

%build
%configure \
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
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang ggz-gtk

%post
%update_menus

%postun
%clean_menus

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -f ggz-gtk.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO README.GGZ QuickStart.GGZ
%{_gamesbindir}/ggz-gtk
%{_datadir}/applications/*
%{_datadir}/ggz/ggz-gtk-client/*
%{_datadir}/ggz/help/*
%{_mandir}/man?/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libggz-gtk.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so


