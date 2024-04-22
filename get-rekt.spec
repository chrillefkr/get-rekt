Name:           get-rekt
Version:        0.0.2
Release:        1%{?dist}
Summary:        Do not install this. It's really bad. Don't.

License:        WTFPL
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc make

%description
Just a SUID wrapper program that runs arguments as root. Sudo without password. Really bad. Don't install.


%global debug_package %{nil}


%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%attr(4111,root,root) %{_sbindir}/get-rekt


%changelog
* Mon Apr 22 2024 Christopher Janzon <christopher.janzon@iver.se> 0.0.2-1
- new package built with tito

* Mon Apr 22 2024 Christopher Janzon <christopher.janzon@iver.se>
- 
