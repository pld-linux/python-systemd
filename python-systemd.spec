#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	systemd
Summary:	Systemd Python 2.x bindings
Summary(pl.UTF-8):	Wiązania do Systemd dla Pythona 2.x
Name:		python-%{module}
Version:	233
Release:	4
Epoch:		1
License:	LGPL
Group:		Development/Languages/Python
Source0:	https://github.com/systemd/python-systemd/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	daa3ecd2c78c538cda7e8c9a7c7d8556
URL:		http://www.freedesktop.org/wiki/Software/systemd
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-lxml
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-lxml
BuildRequires:	python3-modules
BuildRequires:	rpm-build >= 5.4.15-28
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	systemd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Systemd Python 2.x bindings.

%description -l pl.UTF-8
Wiązania do Systemd dla Pythona 2.x.

%package -n python3-%{module}
Summary:	Systemd Python 3.x bindings
Summary(pl.UTF-8):	Wiązania do Systemd dla Pythona 3.x
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
Systemd Python 3.x bindings.

%description -n python3-%{module} -l pl.UTF-8
Wiązania do Systemd dla Pythona 3.x.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%{__rm} -r $RPM_BUILD_ROOT{%{py_sitedir},%{py3_sitedir}}/%{module}/test

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc NEWS README.md
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%{py_sitedir}/%{module}_python-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc NEWS README.md
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}_python-%{version}-py*.egg-info
%endif
