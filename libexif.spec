Summary:	Library for parsing EXIF files from digital cameras
Summary(pl):	Biblioteka do czytania plików EXIF z kamer cyfrowych
Name:		libexif
Version:	0.5.4
Release:	2
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/libexif/%{name}-%{version}.tar.bz2
URL:		http://libexif.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libexif7

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
Obsoletes:	libexif7-devel

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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/%{name}
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
