Summary:	Library for parsing EXIF files from digital cameras
Summary(pl):	Biblioteka do czytania plików EXIF z kamer cyfrowych
Name:		libexif
Version:	0.5.0
Release:	3
License:	MIT license
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/libexif/libexif-0.5.0.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most digital cameras produce EXIF files, which are JPEG files with extra
tags that contain information about the image. The EXIF library allows
you to parse an EXIF file and read the data from those tags.

%description -l pl
Wiêkszo¶æ kamer cyfrowych tworzy pliki EXIF, które s± JPEGami z
dodatkowymi znacznikami zawieraj±cymi informacje o obrazie. Biblioteka
EXIF pozwala czytaæ informacje z tych znaczników.

%package devel
Summary:	Header files for libexif
Summary(pl):	Pliki nag³ówkowe dla libexif
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for libexif.

%description devel -l pl
Pliki nag³ówkowe dla libexif.

%package static
Summary:	Static version of libexif
Summary(pl):	Statyczna wersja libexif
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description static
Static version of libexif.

%description static -l pl
Statyczna wersja libexif.

%prep
%setup -q

%build
autoconf

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.la

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
