Name:           mock-rpmfusion-nonfree
Version:        14.0
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

