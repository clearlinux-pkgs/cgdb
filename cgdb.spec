#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgdb
Version  : 0.6.8
Release  : 7
URL      : http://cgdb.me/files/cgdb-0.6.8.tar.gz
Source0  : http://cgdb.me/files/cgdb-0.6.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: cgdb-bin
Requires: cgdb-data
Requires: cgdb-doc
BuildRequires : bison
BuildRequires : expect
BuildRequires : flex
BuildRequires : help2man
BuildRequires : pkgconfig(ncurses)
BuildRequires : readline-dev
BuildRequires : tcl
BuildRequires : texinfo

%description
CGDB
====
CGDB is a very lightweight console frontend to the GNU debugger.  It provides
a split screen interface showing the GDB session below and the program's
source code above.  The interface is modelled after vim's, so vim users should
feel right at home using it.

%package bin
Summary: bin components for the cgdb package.
Group: Binaries
Requires: cgdb-data

%description bin
bin components for the cgdb package.


%package data
Summary: data components for the cgdb package.
Group: Data

%description data
data components for the cgdb package.


%package doc
Summary: doc components for the cgdb package.
Group: Documentation

%description doc
doc components for the cgdb package.


%prep
%setup -q -n cgdb-0.6.8

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cgdb

%files data
%defattr(-,root,root,-)
/usr/share/cgdb/cgdb.txt

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
