%define name gtkguitune
%define version 0.7
%define release 2mdk

Summary: Guitune is a linux program for tuning guitars
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://www.geocities.com/harpin_floh/kguitune_page.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgtkmm1.2-devel, libstdc++6-devel

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
%setup -q

%build
./configure --prefix=$RPM_BUILD_ROOT%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install
install -m 644 -D guitune $RPM_BUILD_ROOT%{_menudir}/guitune
install -m 644 -D guitune_logo.xpm $RPM_BUILD_ROOT%{_miconsdir}/guitune_logo.xpm

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/gtkguitune
%{_menudir}/guitune
%{_miconsdir}/guitune_logo.xpm

