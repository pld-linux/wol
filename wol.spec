Summary:	Wake On LAN client
Summary(pl):	Klient budzenia przez sieæ
Name:		wol
Version:	0.7.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ahh/%{name}-%{version}.tar.gz
# Source0-md5:	c2fa9d7e771134ac8c89d56b8197d4ca
URL:		http://ahh.sourceforge.net/wol/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wol (Wake On LAN) wakes up magic packet compliant machines such as
boxes with wake-on-LAN ethernet cards.

%description -l pl
wol (budzenie przez sieæ) budzi maszyny zgodne z magicznym pakietem takie
jak komputery z kartami sieciowymi z mo¿liwo¶ci± budzenia-przez-sieæ.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
%{_mandir}/man1/*
