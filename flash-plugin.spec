%global         debug_package %{nil}
%global	        __strip /bin/true

Name:           flash-plugin
Version:        32.0.0.445
Release:        1%{?dist}
Epoch:          1
Summary:        Adobe Flash Player
License:        Non-redistributable, no modification permitted
URL:            http://get.adobe.com/flashplayer/
ExclusiveArch:  %{ix86} x86_64

Source0:        http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash_player_npapi_linux.i386.tar.gz#/%{name}-%{version}-i386.tar.gz
Source1:        http://fpdownload.macromedia.com/get/flashplayer/pdc/%{version}/flash_player_npapi_linux.x86_64.tar.gz#/%{name}-%{version}-x86_64.tar.gz

BuildRequires:  desktop-file-utils
Requires:       mozilla-filesystem

%description
The Adobe Flash Plugin is a freeware Mozilla plugin for viewing multimedia,
executing rich Internet applications, and streaming video and audio, content
created on the Adobe Flash platform.

%package properties
Summary:        Adobe Flash Player preferences
Obsoletes:      %{name}-kde < %{?epoch}:%{version}-%{release}
Provides:       %{name}-kde = %{?epoch}:%{version}-%{release}
Requires:       %{name}%{_isa} = %{?epoch}:%{version}-%{release}
Requires:       hicolor-icon-theme

%description properties
Adobe Flash Player preferences control panel.

%prep
%ifarch %{ix86}
%setup -q -c -n %{name}
%endif

%ifarch x86_64
%setup -q -T -a 1 -c -n %{name}
%endif

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}
cp -afr .%{_datadir}/{icons,applications} %{buildroot}%{_datadir}/

install -p -m 0755 -D .%{_bindir}/flash-player-properties \
    %{buildroot}%{_bindir}/flash-player-properties
install -p -m 0755 -D libflashplayer.so \
    %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so

desktop-file-validate %{buildroot}%{_datadir}/applications/flash-player-properties.desktop

%post properties
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun properties
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans properties
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license license.pdf
%doc readme.txt
%{_libdir}/mozilla/plugins/libflashplayer.so

%files properties
%{_bindir}/flash-player-properties
%{_datadir}/applications/flash-player-properties.desktop
%{_datadir}/icons/hicolor/*/apps/flash-player-properties.png

%changelog
* Fri Oct 30 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.445-1
- Update to 32.0.0.445.

* Tue Oct 06 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.433-1
- Update to 32.0.0.433.

* Sun Aug 16 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.414-1
- Update to 32.0.0.414.

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.403-1
- Update to 32.0.0.403.

* Sat Jun 27 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.387-1
- Update to 32.0.0.387.

* Wed May 20 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.371-1
- Update to 32.0.0.371.

* Mon Apr 27 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.363-1
- Update to 32.0.0.363.

* Fri Mar 27 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.344-1
- Update to 32.0.0.344.
- Trim changelog.

* Tue Feb 11 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.330-1
- Update to 32.0.0.330.

* Mon Jan 27 2020 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.314-1
- Update to 32.0.0.314.

* Thu Dec 19 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.303-1
- Update to 32.0.0.303.

* Sat Nov 16 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.293-1
- Update to 32.0.0.293.

* Thu Oct 31 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.270-1
- Update to 32.0.0.270.

* Sun Sep 29 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.255-1
- Update to 32.0.0.255.

* Sun Aug 18 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.238-1
- Update to 32.0.0.238.

* Tue Jul 09 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.223-1
- Update to 32.0.0.223.

* Fri Jun 21 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.207-1
- Update to 32.0.0.207.

* Tue May 21 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.192-1
- Update to 32.0.0.192.

* Sat Apr 13 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.171-1
- Update to 32.0.0.171.

* Sat Mar 23 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.156-1
- Update to 32.0.0.156.

* Mon Feb 18 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.142-1
- Update to 32.0.0.142.

* Sat Jan 12 2019 Simone Caronni <negativo17@gmail.com> - 1:32.0.0.114-1
- Update to 32.0.0.114.
