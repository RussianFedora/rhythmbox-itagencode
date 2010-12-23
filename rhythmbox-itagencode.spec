Summary:	encode ID3 tags from cp1251 to UTF-8 
Name:		rhythmbox-itagencode
Version:	0.1
Release:	1

License:	GPLv2+
Group:		Applications/Multimedia
URL:		http://code.google.com/p/encodeid3tags/
Source:		http://encodeid3tags.googlecode.com/files/idTagEncode_v01.tar.gz
Source1:	rhythmbox-itagencode.schemas
BuildRoot:	{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	rhythmbox

BuildArch:	noarch

%description
Plugin for gnome music player Rhythmbox - encode ID3 tags from cp1251 to UTF-8 


%prep
%setup -q -n idTagEncode


%build


%install
rm -rf %{buildroot}
install -dD %{buildroot}%{_libdir}/rhythmbox/plugins/idTagEncode
install -dD %{buildroot}%{_sysconfdir}/gconf/schemas/

install -m 644 __init__.py idTagEncode.rb-plugin \
	%{buildroot}%{_libdir}/rhythmbox/plugins/idTagEncode
install -m 644 %{SOURCE1} \
	%{buildroot}%{_sysconfdir}/gconf/schemas/


%clean
rm -rf %{buildroot}


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/rhythmbox-itagencode.schemas >/dev/null


%preun
if [ "$1" -eq 0 ]; then
    export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
    gconftool-2 --makefile-uninstall-rule \
      %{_sysconfdir}/gconf/schemas/rhythmbox-itagencode.schemas > /dev/null || :
fi


%files
%defattr(-, root, root)
%{_libdir}/rhythmbox/plugins/idTagEncode/*
%{_sysconfdir}/gconf/schemas/rhythmbox-itagencode.schemas


%changelog
* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.1-1
- update to 0.1

* Wed Sep 29 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.0-1
- initial build
