%define name zeppoo
%define version 0.0.4
%define release %mkrel 4
%define _requires_exceptions libzeppoo/libzeppoo.so

Summary: Rootkit detection tool
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://downloads.sourceforge.net/zeppoo/%{name}-%{version}.tar.bz2
License: GPL
Group: Monitoring
Url: http://www.zeppoo.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
