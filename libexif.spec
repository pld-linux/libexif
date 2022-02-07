#
# NOTE:
# - exif headers should be included as <libexif/something.h>
#   so don't ,,fix'' pkgconfig file
#
# Conditional build:
%bcond_without	static_libs	# don't build static library

Summary:	Library for parsing EXIF files from digital cameras
Summary(pl.UTF-8):	Biblioteka do czytania plików EXIF z kamer cyfrowych
Name:		libexif
Version:	0.6.24
Release:	1
Epoch:		1
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/libexif/libexif/releases
Source0:	https://github.com/libexif/libexif/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	00ea6e7ff62d3fd41ea9b2139746703c
URL:		https://libexif.github.io/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14.1
BuildRequires:	doxygen
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	libtool >= 2:2
BuildRequires:	rpm-build >= 4.6
Obsoletes:	libexif7 < 0.6
Obsoletes:	libmnote < 0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%description -l pl.UTF-8
Większość kamer cyfrowych tworzy pliki EXIF, które są JPEGami z
dodatkowymi znacznikami zawierającymi informacje o obrazie. Biblioteka
EXIF pozwala czytać informacje z tych znaczników.

%package devel
Summary:	Header files for libexif
Summary(pl.UTF-8):	Pliki nagłówkowe dla libexif
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libexif7-devel < 0.6
Obsoletes:	libmnote-devel < 0.6

%description devel
Header files for libexif.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla libexif.

%package static
Summary:	Static version of libexif
Summary(pl.UTF-8):	Statyczna wersja libexif
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libmnote-static < 0.6

%description static
Static version of libexif.

%description static -l pl.UTF-8
Statyczna wersja libexif.

%package apidocs
Summary:	libexif API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libexif
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for libexif library.

%description apidocs -l pl.UTF-8
Dokumentacja API oraz wewnętrzna dla biblioteki libexif.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}

# docs generation fails with -jN>1
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libexif.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libexif

%find_lang %{name}-12

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-12.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libexif.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libexif.so.12

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libexif.so
%{_includedir}/libexif
%{_pkgconfigdir}/libexif.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libexif.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc doc/doxygen-output/libexif*
