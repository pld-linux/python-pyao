%include        /usr/lib/rpm/macros.python
%define		module pyao
Name:		python-%{module}
Version:	0.81
Release:	1
Summary:	A Python module for the the ao library
Summary(pl):	Modu³ pythona do biblioteki ao
Group:		Libraries/Python
License:	GPL
URL:		http://www.andrewchatham.com/pyogg/
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
Requires:	python-modules
Requires:	libao
BuildRequires:	python-devel
BuildRequires:	libao-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyao

%description
Pyao is a wrapper for libao, an audio device abstraction library.

%description -l pl
Pyao jest wrapperem dla biblioteki libao.

%package devel
Summary:	pyao header and example programs
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Obsoletes:	pyao-devel

%description devel
Pyao is a wrapper for libao, an audio device abstraction library.

Install python-pyogg-devel if you need the API documentation and
example programs.

%description devel -l pl
Pyao jest wrapperem dla biblioteki libao.

Zainstaluj tê paczkê je¶li potrzebujesz dokumentacjê API oraz
przyk³adowe programy.

%prep
%setup -q -n %{module}-%{version}

%build
python config_unix.py \
	--prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_incdir}
python setup.py install \
	--root $RPM_BUILD_ROOT

install src/aomodule.h $RPM_BUILD_ROOT%{py_incdir}

chmod -x test.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{py_sitedir}/*.so
%doc AUTHORS ChangeLog README

%files devel
%defattr(644,root,root,755)
%{py_incdir}/aomodule.h
%doc test.py
