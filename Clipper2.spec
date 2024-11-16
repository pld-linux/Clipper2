Summary:	A Polygon Clipping and Offsetting library
Summary(pl.UTF-8):	Biblioteka do przycinania i przesunięć wielokątów
Name:		Clipper2
Version:	1.4.0
Release:	2
License:	BSL v1.0
Group:		Libraries
#Source0Download: https://github.com/AngusJohnson/Clipper2/releases
Source0:	https://github.com/AngusJohnson/Clipper2/archive/Clipper2_%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8105133391d1a163f19bcc8225990817
URL:		https://github.com/AngusJohnson/Clipper2/
BuildRequires:	cmake >= 3.15
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	gtest-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Polygon Clipping and Offsetting library.

%description -l pl.UTF-8
Biblioteka do przycinania i przesunięć wielokątów.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:7

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n %{name}-%{name}_%{version}

%build
%cmake -B build -S CPP \
	-DCLIPPER2_UTILS=OFF \
	-DCLIPPER2_EXAMPLES=OFF \
	-DUSE_EXTERNAL_GTEST=ON

%{__make} -C build

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
