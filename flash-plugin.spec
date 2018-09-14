%global         debug_package %{nil}
%global	        __strip /bin/true

Name:           flash-plugin
Version:        31.0.0.108
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
* Fri Sep 14 2018 Simone Caronni <negativo17@gmail.com> - 1:31.0.0.108-1
- Update to 31.0.0.108.

* Sun Aug 19 2018 Simone Caronni <negativo17@gmail.com> - 1:30.0.0.154-1
- Update to 30.0.0.154.

* Sat Jul 14 2018 Simone Caronni <negativo17@gmail.com> - 1:30.0.0.134-1
- Update to 30.0.0.134.

* Mon Jun 11 2018 Simone Caronni <negativo17@gmail.com> - 1:30.0.0.113-1
- Update to 30.0.0.113.

* Fri May 11 2018 Simone Caronni <negativo17@gmail.com> - 1:29.0.0.171-1
- Update to 29.0.0.171.

* Thu Apr 12 2018 Simone Caronni <negativo17@gmail.com> - 1:29.0.0.140-1
- Update to 29.0.0.140.

* Thu Mar 15 2018 Simone Caronni <negativo17@gmail.com> - 1:29.0.0.113-1
- Update to 29.0.0.113.

* Thu Feb 08 2018 Simone Caronni <negativo17@gmail.com> - 1:28.0.0.161-1
- Update to 28.0.0.161.

* Fri Jan 19 2018 Simone Caronni <negativo17@gmail.com> - 1:28.0.0.137-1
- Update to 28.0.0.137.

* Thu Dec 14 2017 Simone Caronni <negativo17@gmail.com> - 1:28.0.0.126-1
- Update to 28.0.0.126.

* Fri Nov 17 2017 Simone Caronni <negativo17@gmail.com> - 1:27.0.0.187-1
- Update to 27.0.0.187.

* Wed Nov 01 2017 Simone Caronni <negativo17@gmail.com> - 1:27.0.0.183-1
- Update to version 27.0.0.183.

* Sun Sep 17 2017 Simone Caronni <negativo17@gmail.com> - 1:27.0.0.130-1
- Update to 27.0.0.130.

* Wed Aug 09 2017 Simone Caronni <negativo17@gmail.com> - 1:26.0.0.151-1
- Update to 26.0.0.151.

* Fri Jul 21 2017 Simone Caronni <negativo17@gmail.com> - 1:26.0.0.137-1
- Update to 26.0.0.137.

* Thu Jun 22 2017 Simone Caronni <negativo17@gmail.com> - 1:26.0.0.131-1
- Update to 26.0.0.131.

* Thu Jun 15 2017 Simone Caronni <negativo17@gmail.com> - 1:26.0.0.126-1
- Update to 26.0.0.126.

* Wed May 10 2017 Simone Caronni <negativo17@gmail.com> - 1:25.0.0.171-1
- Update to 25.0.0.171.

* Wed Apr 12 2017 Simone Caronni <negativo17@gmail.com> - 1:25.0.0.148-1
- Update to version 25.0.0.148.

* Tue Mar 14 2017 Simone Caronni <negativo17@gmail.com> - 1:25.0.0.127-1
- Update to 25.0.0.127.

* Wed Feb 15 2017 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.221-1
- Update to 24.0.0.221.

* Wed Jan 11 2017 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.194-1
- Update to 24.0.0.194.

* Fri Dec 16 2016 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.189-1
- Update to 24.0.0.189.

* Thu Dec 08 2016 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.178-1
- Update to beta 24.0.0.178.

* Mon Dec 05 2016 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.170-1
- Update to beta 24.0.0.170.

* Fri Nov 25 2016 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.154-2
- Fix typo in sources.

* Tue Nov 22 2016 Simone Caronni <negativo17@gmail.com> - 1:24.0.0.154-1
- Update to latest beta version 24.0.0.154.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.644-1
- Update to 11.2.202.644.

* Wed Oct 26 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.643-1
- Update to 11.2.202.643.

* Tue Oct 18 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.637-1
- Update to 11.2.202.637.

* Tue Sep 20 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.635-1
- Update to 11.2.202.635.

* Wed Jul 20 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.632-1
- Update to 11.2.202.632.

* Tue Jun 21 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.626-1
- Update to latest 11.2.202.626.

* Mon May 23 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.621-1
- Update to 11.2.202.621.

* Wed Apr 13 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.616-1
- Update to 11.2.202.616.

* Thu Mar 24 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.577-2
- Fix versioning.

* Mon Mar 14 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.577-1
- Update to 11.2.202.577.

* Fri Feb 12 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.569-1
- Update to 11.2.202.569.

* Mon Jan 11 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.559-1
- Fix version.

* Tue Jan 05 2016 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.554-2
- Update to 11.2.202.559.

* Thu Dec 17 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.554-1
- Update to 11.2.202.554.

* Tue Nov 10 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.548-1
- Update to 11.2.202.548.

* Wed Oct 21 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.540-1
- Update to 11.2.202.540.

* Tue Oct 13 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.535-1
- Update to version 11.2.202.535.

* Tue Sep 22 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.521-1
- Update to 11.2.202.521.

* Sat Aug 15 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.508-2
- Update to version 11.2.202.508 for real.

* Thu Aug 13 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.508-1
- Update to 11.2.202.508.

* Mon Jul 20 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.491-1
- Updated to 11.2.202.491.

* Wed Jul 08 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.481-1
- Updated to 11.2.202.481.

* Wed Jun 24 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.468-1
- Update to 11.2.202.468.

* Tue May 12 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.460-1
- Update to 11.2.202.460.

* Fri Apr 17 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.457-1
- Update to 11.2.202.457.

* Mon Mar 30 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.451-1
- Update to 11.2.202.451.

* Thu Feb 05 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.442-1
- Update to 11.2.202.442.

* Thu Jan 29 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.440-1
- Update to 11.2.202.440.

* Fri Jan 23 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.438-1
- Update to 11.2.202.438.

* Wed Jan 14 2015 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.429-1
- Update to 11.2.202.429.

* Sun Dec 14 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.425-1
- Update to 11.2.202.425.

* Wed Nov 26 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.424-1
- Update to 11.2.202.424.

* Fri Oct 17 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.411-1
- Update to 11.2.202.411.

* Tue Sep 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.406-1
- Update to 11.2.202.406.

* Thu Aug 21 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.400-1
- Update to 11.2.202.400.

* Wed Jul 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.394-1
- Update to 11.2.202.394.

* Mon Jun 16 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.378-1
- Update to 11.2.202.378.

* Mon May 19 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.359-1
- Update to 11.2.202.359.

* Wed Apr 30 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.356-1
- Update to 11.2.202.356.

* Thu Apr 10 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.350-1
- Update to 11.2.202.350.

* Wed Mar 12 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.346-1
- Update to 11.2.202.346.

* Thu Mar 06 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.341-1
- Update to 11.2.202.341.

* Sun Feb 09 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.336-1
- Update to 11.2.202.336.

* Wed Jan 29 2014 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.335-1
- Update to 11.2.202.335.

* Sat Dec 14 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.332-1
- Updated to 11.2.202.332.

* Tue Nov 26 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-2
- Review fixes.
- Split flash-plugin-properties package so on x86_64 system there are no 32 bit
  commands.
- Remove kde control center integration (really useless).

* Wed Nov 20 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.327-1
- Updated to 11.2.202.327.

* Tue Sep 24 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.310-1
- Update to 11.2.202.310.

* Mon Jul 15 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.297-1
- Update to 11.2.202.297.

* Wed Jun 26 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.291-1
- Updated to 11.2.202.291.

* Tue May 21 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.285-1
- Updated to 11.2.202.285.

* Mon May 13 2013 Simone Caronni <negativo17@gmail.com> - 1:11.2.202.280-1
- First build.
- Bump epoch to override Adobe official plugin package.
