%define name gtkguitune
%define version 0.8
%define release  5

Summary: Linux program for tuning guitars
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.geocities.com/harpin_floh/mysoft/%{name}-gtk2-%{version}.tar.gz
License: GPLv2+
Group: Sound
Url: http://www.geocities.com/harpin_floh/kguitune_page.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkmm2.4-devel

%description
Guitune is a linux program for tuning guitars and other instruments
by using the method of Schmitt-triggering, i.e.
counting the number of triggerings between two trigger levels
in a certain amount of time.
Why not use FFT like many other tuning devices?
Well because other tuning devices are not as fast as mine !!

With FFT you need many samples to archieve the accuracy needed for tuning
instruments. You often get times of around 1 second between two measurements
and the computer is quite busy in this second calculating the FFT. Using
Schmitt-triggering you get a measurement every 10th of a second or even less
(depending on the sample frequency you use). Most of the time the computer
only waits for the samples.

The Trigger levels are adjustable. For a pure sine-wave the trigger levels
could be zero. But for a wave wth overtones like the one in the figure above
you need a non-zero triggerlevel. It is preadjusted to a level of 60% of the
current maximum which should be able to deal with most instruments.

%prep
%setup -q -n %name

%build
%configure2_5x
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=gtkGuitune
Categories=AudioVideo;GTK;Audio;
Comment=Tune your Guitar
TryExec=gtkguitune
Exec=gtkguitune
Icon=gtkguitune_logo
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdvver < 200900
%post
%update_icon_cache hicolor
%postun
%clean_icon_cache hicolor
%endif

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_bindir}/gtkguitune
%_datadir/icons/hicolor/scalable/apps/guitune_logo.svg
%_datadir/applications/mandriva*



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8-4mdv2011.0
+ Revision: 610992
- rebuild

* Wed Dec 09 2009 JÃ©rÃ´me Brenier <incubusss@mandriva.org> 0.8-3mdv2010.1
+ Revision: 475276
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Oct 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.8-1mdv2009.1
+ Revision: 296418
- new version
- gtkmm 2
- update file list
- add menu entry

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - fix BR for x86_64
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - import gtkguitune

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Sun Sep  5 2004 Jérémie Lenfant-Engelmann <jlenfant@mandrakesoft.com> 0.7-2mdk
- clean spec

* Thu Sep  2 2004 Tocman <jlenfant@mandrakesoft.com> 0.7-1mdk
- First package (pingu1 sux)
