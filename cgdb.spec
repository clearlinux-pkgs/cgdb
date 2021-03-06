#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgdb
Version  : 0.7.1
Release  : 17
URL      : http://cgdb.me/files/cgdb-0.7.1.tar.gz
Source0  : http://cgdb.me/files/cgdb-0.7.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: cgdb-bin = %{version}-%{release}
Requires: cgdb-data = %{version}-%{release}
Requires: cgdb-info = %{version}-%{release}
Requires: cgdb-license = %{version}-%{release}
BuildRequires : bison
BuildRequires : expect
BuildRequires : flex
BuildRequires : help2man
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev
BuildRequires : tcl
BuildRequires : texinfo

%description
No detailed description available

%package bin
Summary: bin components for the cgdb package.
Group: Binaries
Requires: cgdb-data = %{version}-%{release}
Requires: cgdb-license = %{version}-%{release}

%description bin
bin components for the cgdb package.


%package data
Summary: data components for the cgdb package.
Group: Data

%description data
data components for the cgdb package.


%package info
Summary: info components for the cgdb package.
Group: Default

%description info
info components for the cgdb package.


%package license
Summary: license components for the cgdb package.
Group: Default

%description license
license components for the cgdb package.


%prep
%setup -q -n cgdb-0.7.1
cd %{_builddir}/cgdb-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605126077
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605126077
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cgdb
cp %{_builddir}/cgdb-0.7.1/COPYING %{buildroot}/usr/share/package-licenses/cgdb/dfac199a7539a404407098a2541b9482279f690d
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cgdb

%files data
%defattr(-,root,root,-)
/usr/share/cgdb/cgdb.txt

%files info
%defattr(0644,root,root,0755)
/usr/share/info/cgdb.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cgdb/dfac199a7539a404407098a2541b9482279f690d
