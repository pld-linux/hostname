Summary:	Utility to set/show the host name or domain name
Summary(pl.UTF-8):	Narzędzie do ustawiania i sprawdzania nazwy hosta lub domeny
Name:		hostname
Version:	3.21
Release:	1
License:	GPL v2+
Group:		Base
Source0:	http://ftp.debian.org/debian/pool/main/h/hostname/%{name}_%{version}.tar.gz
# Source0-md5:	c89bf2e3f2877e707e8aad8c8e805269
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

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags} -D_GNU_SOURCE" \
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
