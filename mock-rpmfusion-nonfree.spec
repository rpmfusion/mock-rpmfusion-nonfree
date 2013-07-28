Name:           mock-rpmfusion-nonfree
Version:        19.1
Release:        1%{?dist}
Summary:        Mock config files for the RPM Fusion NonFree Repository

Group:          Development/Tools
License:        BSD
URL:            http://rpmfusion.org/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       mock

%description
Mock config files for the RPM Fusion NonFree Repository


%prep
%setup -q -c


%build
#Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mock
install -pm 0644 *.cfg $RPM_BUILD_ROOT%{_sysconfdir}/mock


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mock/*_nonfree.cfg


%changelog
* Sun Jul 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 19.1-1
- Update to 19.1
- Add kernel-override repository - disabled by default

* Tue Apr  2 2013 Nicolas Chauvet <kwizart@gmail.com> - 19.0-1
- Add fedora-19

* Tue Jan  1 2013 Nicolas Chauvet <kwizart@gmail.com> - 18.1-1
- Sync with mock 1.1.28
- Switch to release for F-18
- Fix sparc not available for f18 rfbz#2620

* Thu Sep  6 2012 Nicolas Chauvet <kwizart@gmail.com> - 18.0-1
- Update to 18.0
- Remove fedora-14 and fedora-15
- Fix Rawhide repo - rfbz#2431
- Sync with mock layout (debug repo)

* Sun Jun 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 17.1-1
- Switch baseurl to fedora-secondary
- Fix koji local URL on secondary arches
- Disable testing repos on EL

* Wed Mar  8 2012 Nicolas Chauvet <kwizart@gmail.com> - 17.0-1
- Bump to 17.0
- Introduce armhfp for 15 17 rawhide
- Drop the multilib workaround
- Update dist-f??-build to f??-build

* Sun Jul 31 2011 Nicolas Chauvet <kwizart@fedoraproject.org> - 15.1-1
- Add Support for EL6 - rfbz#1862 & rfbz#1864
- Obsolete F13 config files
- Fix arm local repository
- Add support for branched/f16

* Wed Jun 15 2011 Nicolas Chauvet <kwizart@fedoraproject.org> - 15.0-1
- Update to 15.0
- Sync with mock-1.1.10
- Add secondary arches (arm,sparc,sparc64,s390x).

* Mon Oct 11 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 14.0-1
- Update to 14.0
- Fix syslog user
- Initiate epel-6 files

* Tue Apr 13 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 13.0-1
- Update to 13.0

* Sat Nov 14 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 12.1-1
- Resync with mock 0.19 (update local repos)
- ccache is now available on EL5
- avoid to define the macro 'distribution'
- Add buildsys repos (disabled by default).

* Wed Nov  4 2009 kwizart < kwizart at gmail.com > - 12.0-1
- Update to 12.0 (i686 by default)
- Provides some macros
- Fix fedora koji local repository
- Bump rawhide to fc13

* Wed Sep  2 2009 kwizart < kwizart at gmail.com > - 11.1-1
- Sync epel 4/5 (Moved to koji, removed plague reference)

* Fri Jul 31 2009 kwizart < kwizart at gmail.com > - 11.0-2
- Switch to target i686 on x86 for Rawhide F-12

* Tue May 12 2009 kwizart < kwizart at gmail.com > - 11.0-1
- Branch for F-11

* Wed Mar  4 2009 kwizart < kwizart at gmail.com > - 10.1-1
- Update to 10.1
- Fix Rawhide dist to .f11
- Set Rawhide default target_arch to i586 for x86

* Mon Feb 23 2009 kwizart < kwizart at gmail.com > - 10.0-1
- Bump to 10.0

* Fri Feb 20 2009 kwizart < kwizart at gmail.com > - 0.93-1
- Update to 0.93
- Add need_sign repos (desactivated by default).
- Use the same root as the mother distro.

* Thu Dec 18 2008 kwizart < kwizart at gmail.com > - 0.90-1
- Initial package.

