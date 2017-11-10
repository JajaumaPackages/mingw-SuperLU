%?mingw_package_header

Name:           mingw-SuperLU
Version:        5.2.1
Release:        1%{?dist}
Summary:        MinGW port of SuperLU

License:        BSD
URL:            http://crd-legacy.lbl.gov/~xiaoye/SuperLU
Source0:        http://crd-legacy.lbl.gov/~xiaoye/SuperLU/superlu_%{version}.tar.gz

BuildRequires:  cmake

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-openblas

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-openblas

BuildArch:      noarch

%description
MinGW Windows port of SuperLU.

# Win32
%package -n mingw32-SuperLU
Summary:        32-bit version of SuperLU for Windows

%description -n mingw32-SuperLU
%mingw32_description

# Win64
%package -n mingw64-SuperLU
Summary:        64-bit version of SuperLU for Windows

%description -n mingw64-SuperLU
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn SuperLU_%{version}

%build
%mingw_cmake \
    -Denable_blaslib=OFF \
    -Denable_tests=OFF
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw32_libdir}/*.dll %{buildroot}%{mingw32_bindir}

mkdir -p %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw64_libdir}/*.dll %{buildroot}%{mingw64_bindir}

# Win32
%files -n mingw32-SuperLU
%{mingw32_bindir}/libsuperlu.dll
%{mingw32_includedir}/*.h
%{mingw32_libdir}/libsuperlu.dll.a

# Win64
%files -n mingw64-SuperLU
%{mingw64_bindir}/libsuperlu.dll
%{mingw64_includedir}/*.h
%{mingw64_libdir}/libsuperlu.dll.a

%changelog
* Thu Nov 09 2017 Jajauma's Packages <jajauma@yandex.ru> - 5.2.1-1
- Initial release
