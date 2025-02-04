# RPM spec file for Fedora and openSUSE
%undefine _hardened_build
%define debug_package %{nil}

%global appver 2.1.2
%global build_timestamp %(date "+%%Y%%m%%d%%H%%M%%S")
%global changelog_date Sat Mar 12 2022
%global branch %([[ %{appver} == *"-"* ]] && echo master || echo release)

Name: ghostwriter
Version: %(echo %{appver} | tr '-' '~')
Release: 0.%{build_timestamp}%{?dist}

License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Summary: A distraction-free Markdown editor
URL: https://github.com/wereturtle/%{name}

BuildRequires: git
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: pkgconfig(hunspell)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5XmlPatterns)
%if 0%{?suse_version}
BuildRequires: update-desktop-files
%endif

Requires: hicolor-icon-theme

%description
ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber’s website at http://www.daringfireball.net.

ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%build
rm -rf %{name}
git clone %{url}.git %{name}
cd %{name}
git checkout %{branch}
PREFIX=%{_prefix} qmake-qt5 %{name}.pro
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%endif
%find_lang %{name} --with-qt

%files -f %{name}.lang
%doc CHANGELOG.md CONTRIBUTING.md CREDITS.md README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Sun Jan 3 2021 wereturtle <wereturtledev@gmail.com> - %{appver}
- Upstream release.
