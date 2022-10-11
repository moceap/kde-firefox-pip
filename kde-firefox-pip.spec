Name: kde-firefox-pip
Version: 1
Release: 1%{?dist}
Summary: Custumize Firefox PIP to close perfection in KDE plasma 
License: GPLv3
URL: https://parmg.sa
Source0: LICENSE
Source1: kwinrulesrc
BuildArch: noarch

%description
Custumize Firefox PIP to close perfection in KDE plasma 

%prep
#NOTHING

%install
mkdir -p %{buildroot}%{_configdir}/skel/.config
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_configdir}/skel/.config

%files
%license LICENSE
%{_configdir}/skel/.config/kwinrulesrc

%changelog
* Tue Oct 11 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 2-1
- Initial
