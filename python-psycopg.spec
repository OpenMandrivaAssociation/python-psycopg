%define module psycopg

%define zope_product_path %{_prefix}/lib/zope/lib/python/Products/

Summary:        PostgreSQL database adapter for Python
Name:           python-%module
Version:        1.1.21
Release:        %mkrel 10
Group:          Development/Python
License:        GPL
URL:            http://www.initd.org/software/initd/psycopg
Source0:        http://initd.org/pub/software/psycopg/%{module}-%{version}.tar.bz2
Patch0:		psycopg-1.1.21-linkage.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
# for DateTime
Requires:       python-egenix-mx-base
%py_requires -d
BuildRequires:  postgresql-devel 
BuildRequires:  python-egenix-mx-base

%description
psycopg is a PostgreSQL database adapter for the Python programming
language (just like pygresql and popy.) It was written from scratch with
the aim of being very small and fast, and stable as a rock. The main
advantages of psycopg are that it supports the full Python DBAPI-2.0 and
being thread safe at level 2.

# %package -n zope-ZPsycopgDA
# Summary: Zope postgresql adaptor
# Group: Networking/WWW
# Requires: zope
# Requires: %{name} = %{version}
# 
# %description -n zope-ZPsycopgDA
# Zope postgresql adaptor

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
%configure2_5x \
   --with-mxdatetime-includes=%{py_platsitedir}/mx/DateTime/mxDateTime/
%make

%install
rm -rf %buildroot
mkdir -p $RPM_BUILD_ROOT/%{py_platsitedir}
install -m 755 psycopgmodule.so $RPM_BUILD_ROOT/%{py_platsitedir}

# isntall zope product
# mkdir -p $RPM_BUILD_ROOT/%zope_product_path
# cp -a ZPsycopgDA $RPM_BUILD_ROOT/%zope_product_path

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS  COPYING  CREDITS  FAQ  INSTALL  NEWS  README  RELEASE-1.0  SUCCESS  TODO doc
%{py_platsitedir}/*.so

# %files -n zope-ZPsycopgDA
# %defattr(-,root,root,-)
# %zope_product_path/ZPsycopgDA



