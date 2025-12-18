%global application_name waterfox
%global internal_name waterfox

Name:           %{application_name}
Version: null
Release:        1%{?dist}
Summary:        Waterfox Web Browser

License:        MPL-2.0
URL:            https://www.waterfox.net/
Source0:        https://cdn1.waterfox.net/waterfox/releases/%{version}/Linux_x86_64/waterfox-%{version}.tar.bz2
Source1:        waterfox.desktop
Source2:        policies.json
Source3:        LICENSE
Source4:        README.md

BuildArch:      x86_64
Requires:       libX11

%description
Waterfox is an open-source, privacy-focused browser based on the popular open source browser with a red panda as a mascot.
It is designed to be a drop-in replacement for said browser, offering enhanced privacy features, performance improvements,
and customizability while maintaining compatibility with existing extensions.

Bugs in Waterfox should be reported to Waterfox Github repo:
https://github.com/BrowserWorks/waterfox/issues

Bugs in this RPM repo should be reported here:
https://github.com/maiykill/waterfox-rpm/issues

%prep
# The tarball unpacks into 'waterfox/' directory
%setup -q -n %{application_name}

%build
# No build needed, prebuilt binaries used

%install
rm -rf %{buildroot}

# Install application files under /opt/waterfox (literal absolute path)
mkdir -p %{buildroot}/opt/%{application_name}
cp -a * %{buildroot}/opt/%{application_name}/

# Install policies.json to /opt/waterfox/distribution/policies.json
mkdir -p %{buildroot}/opt/%{application_name}/distribution
cp %{SOURCE2} %{buildroot}/opt/%{application_name}/distribution/policies.json

# Create symlink for executable in %{_bindir} (usually /usr/bin)
mkdir -p %{buildroot}%{_bindir}
ln -s /opt/%{application_name}/waterfox %{buildroot}%{_bindir}/%{internal_name}

# Install all icon sizes with corrected source paths
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/22x22/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default22.png %{buildroot}%{_datadir}/icons/hicolor/22x22/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default24.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/waterfox.png

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
cp %{_builddir}/%{application_name}/browser/chrome/icons/default/default256.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/waterfox.png

# Install the desktop entry file
mkdir -p %{buildroot}%{_datadir}/applications
cp %{SOURCE1} %{buildroot}%{_datadir}/applications/waterfox.desktop

# Install documentation files
mkdir -p %{buildroot}%{_docdir}/%{application_name}
cp %{SOURCE3} %{buildroot}%{_docdir}/%{application_name}/LICENSE
cp %{SOURCE4} %{buildroot}%{_docdir}/%{application_name}/README.md

%clean
rm -rf %{buildroot}

%files
%dir /opt/%{application_name}
/opt/%{application_name}/*
%{_bindir}/%{internal_name}
%{_datadir}/icons/hicolor/16x16/apps/waterfox.png
%{_datadir}/icons/hicolor/22x22/apps/waterfox.png
%{_datadir}/icons/hicolor/24x24/apps/waterfox.png
%{_datadir}/icons/hicolor/32x32/apps/waterfox.png
%{_datadir}/icons/hicolor/48x48/apps/waterfox.png
%{_datadir}/icons/hicolor/64x64/apps/waterfox.png
%{_datadir}/icons/hicolor/128x128/apps/waterfox.png
%{_datadir}/icons/hicolor/256x256/apps/waterfox.png
%{_datadir}/applications/waterfox.desktop
%doc %{_docdir}/%{application_name}/LICENSE
%doc %{_docdir}/%{application_name}/README.md

%changelog
* Thu Dec 18 2025 build-bot <actions-build-bot@github.com> - null-1
- Updated to Waterfox null
* Wed Dec 17 2025 build-bot <actions-build-bot@github.com> - 6.6.6-1
- Updated to Waterfox 6.6.6
* Wed Dec 17 2025 build-bot <actions-build-bot@github.com> - null-1
- Updated to Waterfox null
* Tue Dec 09 2025 build-bot <actions-build-bot@github.com> - 6.6.6-1
- Updated to Waterfox 6.6.6
* Tue Nov 25 2025 build-bot <actions-build-bot@github.com> - 6.6.5.1-1
- Updated to Waterfox 6.6.5.1
* Mon Nov 10 2025 build-bot <actions-build-bot@github.com> - 6.6.5-1
- Updated to Waterfox 6.6.5
* Thu Oct 09 2025 build-bot <actions-build-bot@github.com> - 6.6.4-1
- Updated to Waterfox 6.6.4
* Thu Sep 11 2025 build-bot <actions-build-bot@github.com> - 6.6.3-1
- Updated to Waterfox 6.6.3
* Fri Aug 29 2025 build-bot <actions-build-bot@github.com> - 6.6.2-1
- Updated to Waterfox 6.6.2
* Thu Aug 21 2025 build-bot <actions-build-bot@github.com> - 6.6.1-1
- Updated to Waterfox 6.6.1
* Tue Aug 19 2025 build-bot <actions-build-bot@github.com> - 6.6.0-1
- Updated to Waterfox 6.6.0
* Mon Jul 28 2025 build-bot <actions-build-bot@github.com> - 6.5.11-1
- Updated to Waterfox 6.5.11
* Sun Jul 27 2025 build-bot <actions-build-bot@github.com> - 6.5.10-1
- Updated to Waterfox 6.5.10
* Sat Jul 26 2025 maiykill <70015530+maiykill@users.noreply.github.com> - 6.5.10-1
- Initial build of Waterfox 6.5.10 with policies.json and docs included

