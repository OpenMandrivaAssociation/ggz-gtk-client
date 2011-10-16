%define name	ggz-gtk-client
%define version 0.0.14.1
%define release %mkrel 11

%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

%define libggz_version %{version}

%define ggz_client_libs_version %{version}

Name:		%{name}
Summary:	GGZ Client with GTK+ user interface
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

# http://download.sf.net/ggz/
Source:		%{name}-%{version}.tar.bz2
Patch0:		ggz-gtk-client-0.0.14.1-linkage_fix.diff
BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
BuildRequires:	gtk+2-devel desktop-file-utils
Requires:	libggz = %{libggz_version}
Requires:	ggz-client-libs = %{ggz_client_libs_version}
Suggests:	ggz-game-modules = %{version}

%description
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{libname}
Summary:	GGZ Library client with GTK+ user interface
Group:		Games/Other
Obsoletes:	%mklibname %{name} < 0.0.14.1-2

%description -n	%{libname}
The official GGZ Gaming Zone client with GTK+ user interface.

%package -n	%{develname}
Summary:	Development files for GGZ Gaming Zone client with GTK+ user interface
Group:		Development/Other
Requires:	%{libname} = %{version}
Requires:	libggz-devel = %{libggz_version}
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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
%{_libdir}/libggz-gtk.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/lib*.so
