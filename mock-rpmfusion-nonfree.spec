Name:           mock-rpmfusion-nonfree
Version:        10.0
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
* Mon Feb 23 2009 kwizart < kwizart at gmail.com > - 10.0-1
- Bump to 10.0

* Fri Feb 20 2009 kwizart < kwizart at gmail.com > - 0.93-1
- Update to 0.93
- Add need_sign repos (desactivated by default).
- Use the same root as the mother distro.

* Thu Dec 18 2008 kwizart < kwizart at gmail.com > - 0.90-1
- Initial package.

