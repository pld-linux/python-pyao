%define		module	pyao
Summary:	A Python module for the the ao library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki ao
Name:		python-%{module}
Version:	0.82
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://ekyo.nerim.net/software/pyogg/%{module}-%{version}.tar.gz
# Source0-md5:	8e00f5154401a6f6d99efd20606e2819
URL:		http://ekyo.nerim.net/software/pyogg/index.html
BuildRequires:	libao-devel
BuildRequires:	python-devel
Requires:	python-modules
Obsoletes:	pyao
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyao is a wrapper for libao, an audio device abstraction library.

%description -l pl.UTF-8
Pyao jest wrapperem dla libao - biblioteki abstrakcji do odtwarzania
dźwięku.

%package devel
Summary:	pyao header and example programs
Summary(pl.UTF-8):	Plik nagłówkowy i przykładowy program do pyao
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	libao-devel
Obsoletes:	pyao-devel

%description devel
Pyao is a wrapper for libao, an audio device abstraction library. This
package contains the header file and example program for pyao.

%description devel -l pl.UTF-8
Pyao jest wrapperem dla libao - biblioteki abstrakcji do odtwarzania
dźwięku. Ten pakiet zawiera plik nagłówkowy i przykładowy program dla
modułu pyao.

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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root $RPM_BUILD_ROOT

install src/aomodule.h $RPM_BUILD_ROOT%{py_incdir}

chmod -x test.py
install test.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{py_sitedir}/*.so

%files devel
%defattr(644,root,root,755)
%{py_incdir}/aomodule.h
