Summary:	Library for parsing EXIF files from digital cameras
Summary(pl):	Biblioteka do czytania plik�w EXIF z kamer cyfrowych
Name:		libexif
Version:	0.6.9
Release:	1
Epoch:		1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/libexif/%{name}-%{version}.tar.gz
# Source0-md5:	0aa142335a8a00c32bb6c7dbfe95fc24
URL:		http://libexif.sourceforge.net/
BuildRequires:	automake
Obsoletes:	libexif7
Obsoletes:	libmnote
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most digital cameras produce EXIF files, which are JPEG files with
extra tags that contain information about the image. The EXIF library
allows you to parse an EXIF file and read the data from those tags.

%description -l pl
Wi�kszo�� kamer cyfrowych tworzy pliki EXIF, kt�re s� JPEGami z
dodatkowymi znacznikami zawieraj�cymi informacje o obrazie. Biblioteka
EXIF pozwala czyta� informacje z tych znacznik�w.

%package devel
Summary:	Header files for libexif
Summary(pl):	Pliki nag��wkowe dla libexif
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	libexif7-devel
Obsoletes:	libmnote-devel

%description devel
Header files for libexif.

%description devel -l pl
Pliki nag��wkowe dla libexif.

%package static
Summary:	Static version of libexif
Summary(pl):	Statyczna wersja libexif
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	libmnote-static

%description static
Static version of libexif.

%description static -l pl
Statyczna wersja libexif.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
