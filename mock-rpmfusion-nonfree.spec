Name:           mock-rpmfusion-nonfree
Version:        42.1
Release:        1%{?dist}
Summary:        Mock config files for the RPM Fusion NonFree Repository

License:        BSD
URL:            https://rpmfusion.org/
Source0:        https://github.com/rpmfusion-infra/mock-rpmfusion/releases/download/%{version}/%{name}-%{version}.tar.bz2

BuildArch:      noarch
Requires:       mock-rpmfusion-free >= 42.1

%description
Mock config files for the RPM Fusion NonFree Repository


%prep
%setup -q -c


%build
#Nothing to build


%install
mkdir -p %{buildroot}%{_sysconfdir}
cp -a etc/mock %{buildroot}%{_sysconfdir}/mock/


%files
%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/mock/templates/*.tpl


%changelog
* Sun Apr 13 2025 Sérgio Basto <sergio@serjux.com> - 42.1-1
- F42 GA
    
* Sun Feb 09 2025 Sérgio Basto <sergio@serjux.com> - 42.0-1
- F42 branched

* Sun Oct 27 2024 Sérgio Basto <sergio@serjux.com> - 41.1-1
- F41 GA

* Thu Oct 03 2024 Sérgio Basto <sergio@serjux.com> - 41.0-1
- F41 Branched

* Sat Apr 20 2024 Sérgio Basto <sergio@serjux.com> - 40.1-1
- F40 GA

* Thu Feb 15 2024 Sérgio Basto <sergio@serjux.com> - 40.0-1
- F40 Branched

* Sun Nov 05 2023 Sérgio Basto <sergio@serjux.com> - 39.1-1
- F39 GA

* Sun Sep 24 2023 Sérgio Basto <sergio@serjux.com> - 39.0-1
- F39 Branched

* Mon Jun 19 2023 Sérgio Basto <sergio@serjux.com> - 38.1-2
- Add cisco repo for ffmpeg deps

* Tue Apr 18 2023 Sérgio Basto <sergio@serjux.com> - 38.1-1
- F38 GA

* Wed Feb 22 2023 Sérgio Basto <sergio@serjux.com> - 38.0-1
- F38 Branched

* Sat Nov 19 2022 Sérgio Basto <sergio@serjux.com> - 37.2-1
- F37 GA

* Sat Sep 24 2022 Sérgio Basto <sergio@serjux.com> - 37.1-1
- New names for configurations (%{reponame}-%{version}-%{arch}.cfg)
- Make links to short names of settings names in el
- Add links from old configuration names to new names for backwards compatibility.

* Mon Sep 19 2022 Sérgio Basto <sergio@serjux.com> - 37.0-1
- F37 branch

* Sun May 01 2022 Sérgio Basto <sergio@serjux.com> - 36.1-1
- F36 GA
- Add el9 repos

* Sun Feb 13 2022 Sérgio Basto <sergio@serjux.com> - 36.0-1
- F36 branch
- Drop kwizart repo (#21)
- Add support for EPEL-next (#20)

* Tue Nov 02 2021 Sérgio Basto <sergio@serjux.com> - 35.3-1
- RPM Fusion F35 Release

* Wed Oct 13 2021 Sérgio Basto <sergio@serjux.com> - 35.2-1
- Templating

* Mon Sep 13 2021 Sérgio Basto <sergio@serjux.com> - 35.1-1
- v2 of add gpgcheck on updates-testing, debuginfo and branched repos
  commit 373c52a was incompleted
- Also add buildsys-override repos on rawhide

* Sun Aug 15 2021 Sérgio Basto <sergio@serjux.com> - 35.0-1
- F35 Branched
- Add gpgcheck on updates-testing, debuginfo and branched repos

* Tue Apr 27 2021 Sérgio Basto <sergio@serjux.com> - 34.1-1
- F34 GA

* Fri Feb 12 2021 Sérgio Basto <sergio@serjux.com> - 34.0-1
- F34 branched

* Sun Jan 17 2021 Sérgio Basto <sergio@serjux.com> - 33.2-1
- Remove sslcacert on mock configurations because we don't need it anymore,
  koji have a LE certificate

* Fri Oct 16 2020 Sérgio Basto <sergio@serjux.com> - 33.1-1
- F33 GA

* Sat Aug 22 2020 Sérgio Basto <sergio@serjux.com> - 33.0-1
- F33 Branch

* Wed Jun 10 2020 Sérgio Basto <sergio@serjux.com> - 32.3-1
- Make sslcacert on mock configurations work again

* Wed Apr 29 2020 Sérgio Basto <sergio@serjux.com> - 32.2-1
- F32 GA

* Sun Feb 23 2020 Sérgio Basto <sergio@serjux.com> - 32.1-1
- Configurations for Mock-2.0

* Tue Feb 18 2020 Sérgio Basto <sergio@serjux.com> - 32.0-1
- F32 Branch and the forgotten F31 GA

* Thu Dec 26 2019 Sérgio Basto <sergio@serjux.com> - 31.2-1
- Allow --enablerepo=rpmfusion-{non,}free-override to work out of the box

* Tue Sep 24 2019 Sérgio Basto <sergio@serjux.com> - 31.1-2
- Requires mock-core-configs >= 31.4

* Tue Sep 24 2019 Sérgio Basto <sergio@serjux.com> - 31.1-1
- And Centos 8

* Mon Aug 26 2019 Sérgio Basto <sergio@serjux.com> - 31.0-1
- F31 Branch

* Tue May 07 2019 Sérgio Basto <sergio@serjux.com> - 30.2-1
- F30 GA

* Tue Apr 02 2019 Sérgio Basto <sergio@serjux.com> - 30.1-1
- RPMFusion F30 is branched

* Wed Mar 06 2019 Sérgio Basto <sergio@serjux.com> - 30.0-1
- RPMFusion Rawhide pointing to F30 branched

* Mon Oct 29 2018 Sérgio Basto <sergio@serjux.com> - 29.1-1
- F29 GA

* Thu Aug 30 2018 Sérgio Basto <sergio@serjux.com> - 29.0-1
- Add F29 branch and drop F26
- Not include s390x configs (RPMFusion don't have it)
- Include README.txt to help on make these packages.
- Requires: mock-core-configs >= @VERSION@ instead mock itself

* Sat Jun 02 2018 Sérgio Basto <sergio@serjux.com> - 28.1-2
- Fix changelog version

* Fri Jun 01 2018 Sérgio Basto <sergio@serjux.com> - 28.1-1
- make (for F28 GA)
- F28 is not branched anymore
- In nonfree use include free repo instead of copy it
- In kwizart repo use include nonfree repo instead copy free and nonfree repos
- Rename templates to match with the name of repos to simplify the script
- Move branched-templates from not_in_use dir and update it

* Mon Mar 05 2018 Sérgio Basto <sergio@serjux.com> - 28.0-1
- Ready for branch F28

* Fri Feb 23 2018 Sérgio Basto <sergio@serjux.com> - 27.1-1
- Move rpmfusion buildroot to branch F28
- Prepare new version and drop F25
- Fix locations of fedora-secondary arches

* Tue Aug 22 2017 Sérgio Basto <sergio@serjux.com> - 27.0-1
- Add configuration files for Fedora 27
- Remove Configuration files for Fedora 24

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 02 2017 Sérgio Basto <sergio@serjux.com> - 26.0-1
- Add configuration files for Fedora 26
- Remove Configuration files for Fedora 23

* Thu Jan 05 2017 Sérgio Basto <sergio@serjux.com> - 25.2-1
- Fix el-round.sh typo
- Not include rpmfusion-buildsys-epel-template
  This template may will be need when we got back kmod building, we will need
  a special repo with new kernels until have something like it, we dont need this
  template, buildsys_override repos for each branch is in
  rpmfusion-free-epel-template and rpmfusion-nonfree-epel-template, also add
  configure: cost=2000 like in other cases of koji configurations.
- Print and remove obsoleted .cfg files.
- Enable gpgkeys
- Switch to metalink over https
- Organization: move all .cfg files to etc/mock directory
- Organization: Move templates not in use to not_in_use directory
- Update *.spec.in files according new locations of files.
- Clean trailings whitespaces.
- Clean up/modernize spec file, use %{buildroot} macro
- Also run ./round.sh and ./el-round.sh with make

* Thu Nov 10 2016 Sérgio Basto <sergio@serjux.com> - 25.1-1
- Update package requires to mock >= 1.2.19
- Bug fix.
- Add local repo, useful for epel builds.
- Use include include statement

* Tue Aug 09 2016 Sérgio Basto <sergio@serjux.com> - 25.0-1
- Update to 25.0

* Fri Jul  1 2016 Nicolas Chauvet <kwizart@gmail.com> - 24.0-1
- Update to 24.0

* Tue Nov 10 2015 Nicolas Chauvet <kwizart@gmail.com> - 23.0-1
- Update to 23.0

* Sun May 24 2015 Nicolas Chauvet <kwizart@gmail.com> - 22.0-1
- Update to 22.0

* Sun Dec  7 2014 Nicolas Chauvet <kwizart@gmail.com> - 21.0-1
- Update to 21.0
- Fix armhfp is primary since f20
- sync with fedora mock

* Sat Mar 15 2014 Nicolas Chauvet <kwizart@gmail.com> - 20.1-1
- Fix rawhide kernel-nodebug - rfbz#3127
- Drop rawhide sparc
- sync with mock for fedora and el
- Introduce preliminary config for el7

* Sun Dec 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 20.0-1
- Update to 20.0
- Add rpmfusion-kernel-devel-override
- Drop fedora-17
- Drop arm with fedora-19 (only keep armhfp)

* Sun Jul 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 19.2-1
- Update to 19.2
- Add rawhide-kernel-nodebug

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

* Thu Mar  8 2012 Nicolas Chauvet <kwizart@gmail.com> - 17.0-1
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

