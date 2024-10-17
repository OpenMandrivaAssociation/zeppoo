%if %{_use_internal_dependency_generator}
%define __noautoreq 'libzeppoo/libzeppoo.so'
%else
%define _requires_exceptions libzeppoo/libzeppoo.so
%endif

Summary: Rootkit detection tool
Name:    zeppoo
Version: 0.0.4
Release: 6
Source0: http://downloads.sourceforge.net/zeppoo/%{name}-%{version}.tar.bz2
License: GPL
Group: Monitoring
Url: https://www.zeppoo.net/

%description
Zeppoo allows you to detect rootkits on the i386 architecture under
Linux by using /dev/kmem and /dev/mem. It can also detect hidden
tasks, modules, syscalls, some corrupted symbols, and hidden
connections.

%prep
%setup -q

%build
%make -C lib%{name}
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m755 %{name} %{buildroot}%{_bindir}/%{name}.real
cat <<EOF > %{buildroot}%{_bindir}/%{name}
#!/bin/sh
cd %{_libdir}
exec %{name}.real "\$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}
install -D -m644 lib%{name}/lib%{name}.so %{buildroot}%{_libdir}/lib%{name}/lib%{name}.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS Changelog FAQ README SUPPORTS TODO
%{_bindir}/%{name}
%{_bindir}/%{name}.real
%dir %{_libdir}/lib%{name}
%{_libdir}/lib%{name}/lib%{name}.so


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.0.4-5mdv2010.0
+ Revision: 435378
- rebuild

* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.0.4-4mdv2009.0
+ Revision: 263015
- rebuild
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 0.0.4-1mdv2008.1
+ Revision: 141006
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 10 2007 Olivier Blin <oblin@mandriva.com> 0.0.4-1mdv2008.0
+ Revision: 61049
- initial (hackish) release
- Create zeppoo

