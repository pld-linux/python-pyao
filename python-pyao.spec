%include        /usr/lib/rpm/macros.python
%define		module pyao
Summary:	A Python module for the the ao library
Summary(pl):	Modu³ pythona do biblioteki ao
Name:		python-%{module}
Version:	0.81
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.andrewchatham.com/pyogg/download/%{module}-%{version}.tar.gz
URL:		http://www.andrewchatham.com/pyogg/
BuildRequires:	libao-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	pyao

%description
Pyao is a wrapper for libao, an audio device abstraction library.

%description -l pl
Pyao jest wrapperem dla libao - biblioteki abstrakcji do odtwarzania
d¼wiêku.

%package devel
Summary:	pyao header and example programs
Summary(pl):	Plik nag³ówkowy i przyk³adowy program do pyao
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	libao-devel
Obsoletes:	pyao-devel

%description devel
Pyao is a wrapper for libao, an audio device abstraction library. This
package contains the header file and example program for pyao.

%description devel -l pl
Pyao jest wrapperem dla libao - biblioteki abstrakcji do odtwarzania
d¼wiêku. Ten pakiet zawiera plik nag³ówkowy i przyk³adowy program dla
modu³u pyao.

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
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/*.so

%files devel
%defattr(644,root,root,755)
%doc test.py
%{py_incdir}/aomodule.h
