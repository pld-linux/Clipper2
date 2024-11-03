Summary:	A Polygon Clipping and Offsetting library
Name:		Clipper2
Version:	1.4.0
Release:	1
License:	BSL-1.0
Group:		Libraries
Source0:	https://github.com/AngusJohnson/Clipper2/archive/Clipper2_%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8105133391d1a163f19bcc8225990817
URL:		https://github.com/AngusJohnson/Clipper2/
BuildRequires:	cmake
BuildRequires:	gtest-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{name}-%{name}_%{version}

%build
mkdir -p build
cd build
%cmake ../CPP \
	-DCLIPPER2_UTILS=OFF \
	-DCLIPPER2_EXAMPLES=OFF \
	-DUSE_EXTERNAL_GTEST=ON \
	-DBUILD_SHARED_LIBS=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__sed} -i -e '/Cflags:/ s/$/ -DUSINGZ/' $RPM_BUILD_ROOT%{_pkgconfigdir}/Clipper2Z.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libClipper2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libClipper2.so.1
%attr(755,root,root) %{_libdir}/libClipper2Z.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libClipper2Z.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libClipper2.so
%attr(755,root,root) %{_libdir}/libClipper2Z.so
%{_includedir}/clipper2
%{_libdir}/cmake/clipper2
%{_pkgconfigdir}/Clipper2.pc
%{_pkgconfigdir}/Clipper2Z.pc
