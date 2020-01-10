%define glib2_version 2.16.0
%define dbus_version 1.0
%define gcrypt_version 1.2.2

Summary: Framework for managing passwords and other secrets
Name: libgnome-keyring
Version: 3.8.0
Release: 3%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Libraries
#VCS: git:git://git.gnome.org/libgnome-keyring
Source: http://download.gnome.org/sources/libgnome-keyring/3.8/libgnome-keyring-%{version}.tar.xz
URL: http://live.gnome.org/GnomeKeyring


BuildRequires: glib2-devel >= %{glib2_version}
BuildRequires: dbus-devel >= %{dbus_version}
BuildRequires: libgcrypt-devel >= %{gcrypt_version}
BuildRequires: intltool
BuildRequires: gobject-introspection-devel
Conflicts: gnome-keyring < 2.29.4


%description
gnome-keyring is a program that keep password and other secrets for
users. The library libgnome-keyring is used by applications to integrate
with the gnome-keyring system.

%package devel
Summary: Development files for libgnome-keyring
License: LGPLv2+
Group: Development/Libraries
Requires: %name = %{version}-%{release}
Requires: glib2-devel
Conflicts: gnome-keyring-devel < 2.29.4

%description devel
The libgnome-keyring-devel package contains the libraries and
header files needed to develop applications that use libgnome-keyring.


%prep
%setup -q -n libgnome-keyring-%{version}


%build
%configure --disable-gtk-doc --enable-introspection=yes

# avoid unneeded direct dependencies
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang libgnome-keyring


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files -f libgnome-keyring.lang
%doc AUTHORS NEWS README COPYING HACKING
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0
%doc %{_datadir}/gtk-doc/


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 3.8.0-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.8.0-2
- Mass rebuild 2013-12-27

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar  7 2013 Matthias Clasen <mclasen@redhat.com> - 3.7.91-1
- Update to 3.7.91

* Wed Feb 06 2013 Kalev Lember <kalevlember@gmail.com> - 3.7.5-1
- Update to 3.7.5

* Wed Jan 09 2013 Richard Hughes <hughsient@gmail.com> - 3.7.2-1
- Update to 3.7.2

* Wed Sep 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.6.0-1
- Update to 3.6.0

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.6-1
- Update to 3.5.6

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Wed Apr 18 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.4.1-2
- Enable introspection

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Debarshi Ray <rishi@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Fri Mar  9 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.91-1
- Update to 3.3.91

* Tue Feb  7 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.5-1
- Update to 3.3.5

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.4-1
- Update to 3.3.4

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 20 2011 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Thu Nov 24 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.2.2-1
- Update to 3.2.2

* Mon Sep 26 2011 Ray <rstrode@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Mon Sep 19 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.92-1
- Update to 3.1.92

* Wed Aug 31 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.90-1
- Update to 3.1.90

* Tue Jul 26 2011 Matthias Clasen <mclasen@redhat.com> - 3.1.4-1
- Update to 3.1.4

* Mon May  9 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.1-1
- Update to 3.1.1

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Mon Mar 21 2011 Matthias Clasen <mclasen@redhat.com> - 2.91.93-1
- Update to 2.91.93

* Fri Mar 11 2011 Tomas Bzatek <tbzatek@redhat.com> - 2.91.92-1
- Update to 2.91.92

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 28 2010 Matthias Clasen <mclasen@redhat.com> - 2.32.0-1
- Update to 2.32.0

* Mon Sep 13 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.31.92-1
- Update to 2.31.92

* Tue Aug 31 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.91-1
- Update to 2.31.91

* Tue Apr 27 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Mon Apr 19 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.30.0-2
- Workaround for problem with endless loop during blocking operations (#573202)

* Tue Mar 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Mar 22 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.92-git20100322.1
- Update to a new git snapshot

* Wed Mar 17 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.92-git20100317.1
- Update to 2.29.92 git snapshot

* Wed Feb 17 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.4-4
- When no password is found, return GNOME_KEYRING_RESULT_NO_MATCH

* Tue Feb 16 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.4-3
- Fix assertion when password is not found

* Mon Jan 25 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.4-2
- Fix assertion calling deprecated acl function
- Clear the client's session when the service disconnects
- Implement setting of Type property in gnome_keyring_item_set_info()

* Thu Jan  7 2010 Tomas Bzatek <tbzatek@redhat.com> - 2.29.4-1
- Initial packaging
