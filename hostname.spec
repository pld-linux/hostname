Summary:	Utility to set/show the host name or domain name
Summary(pl.UTF-8):	Narzędzie do ustawiania i sprawdzania nazwy hosta lub domeny
Name:		hostname
Version:	3.11
Release:	1
License:	GPL v2+
Group:		Base
Source0:	ftp://ftp.debian.org/debian/pool/main/h/hostname/%{name}_%{version}.tar.gz
# Source0-md5:	4abb765cb25e0315aa17dece62275e92
Patch1:		%{name}-rh.patch
URL:		http://packages.qa.debian.org/h/hostname.html
BuildRequires:	iconv
Conflicts:	net-tools < 1.60-32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides commands which can be used to display the
system's DNS name, and to display or set its hostname or NIS domain
name.

%description -l pl.UTF-8
Ten pakiet udostępnia polecenia służące do wypisywania nazwy DNS
systemu oraz ustawiania nazwy hosta lub domeny NIS.

%prep
%setup -q -n %{name}
%patch1 -p1

iconv -f iso-8859-1 -t utf-8 -o hostname.tmp hostname.1.fr && mv hostname.tmp hostname.1.fr

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT debian/changelog
%attr(755,root,root) /bin/dnsdomainname
%attr(755,root,root) /bin/domainname
%attr(755,root,root) /bin/hostname
%attr(755,root,root) /bin/nisdomainname
%attr(755,root,root) /bin/ypdomainname
%{_mandir}/man1/dnsdomainname.1*
%{_mandir}/man1/domainname.1*
%{_mandir}/man1/hostname.1*
%{_mandir}/man1/nisdomainname.1*
%{_mandir}/man1/ypdomainname.1*
%lang(fr) %{_mandir}/fr/man1/*.1*