Summary:	Utility to set/show the host name or domain name
Name:		hostname
Version:	3.05
Release:	1
License:	GPL v2+
Group:		Base
URL:		http://packages.qa.debian.org/h/hostname.html
Source0:	ftp://ftp.debian.org/debian/pool/main/h/hostname/%{name}_%{version}.tar.gz
# Source0-md5:	28f5bf5c4a494b83ca6f106bd472dcb2
Patch1:		%{name}-rh.patch
BuildRequires:	iconv
Conflicts:	net-tools < 1.60-32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides commands which can be used to display the
system's DNS name, and to display or set its hostname or NIS domain
name.

%prep
%setup -q
%patch1 -p1 -b .rh

iconv -f iso-8859-1 -t utf-8 -o hostname.tmp hostname.1.fr && mv hostname.tmp hostname.1.fr

%build
export CFLAGS="$RPM_OPT_FLAGS $CFLAGS"
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BASEDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT
%attr(755,root,root) /bin/dnsdomainname
%attr(755,root,root) /bin/domainname
%attr(755,root,root) /bin/hostname
%attr(755,root,root) /bin/nisdomainname
%attr(755,root,root) /bin/ypdomainname
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/*.1*
