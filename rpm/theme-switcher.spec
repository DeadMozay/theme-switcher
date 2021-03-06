%global commit      f45bd1a68029bc36c93ab8ec3fbfaf1185b2429f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191109

%global uuid        com.github.Latesil.%{name}

Name:           theme-switcher
Version:        1.0.0
Release:        1.%{date}git%{shortcommit}%{?dist}
Summary:        Switch dark/light GTK theme automatically during day/night

License:        GPLv3+
URL:            https://github.com/Latesil/theme-switcher
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
%if 0%{?fedora}
BuildRequires:  libappstream-glib
%endif
BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  python3-devel
BuildRequires:  systemd
BuildRequires:  pkgconfig(glib-2.0)
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject

%description
A global automated switcher for dark/light GTK theme during day/night and more.

Theme-switcher automatically can switch your:

- GTK theme
- GNOME Terminal profiles
- Wallpapers
- More will come...

To read docs run:

  xdg-open %{_docdir}/%{name}/README.md


%prep
%autosetup -n %{name}-%{commit}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
%if 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE
%doc README.md CREDITS
%{_bindir}/%{name}-auto.sh
%{_bindir}/%{name}-manual.sh
%{_bindir}/%{name}-gui
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/symbolic/*/*.svg
%{_datadir}/%{name}/
%{_metainfodir}/*.xml
%{_userunitdir}/%{name}-auto.*


%changelog
* Fri Nov 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.0.0-1.20191109gitf45bd1a
- Update to 1.0.0

* Mon Nov 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20191104git7ec63be
- Update to latest git snapshot

* Sat Nov 02 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20191102git0e9c4e0
- Update to latest git snapshot

* Wed Jul 31 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9.1-1.20190801git570f378
- Update to latest git snapshot

* Sun Jul 28 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-8.20190728gitb1a6284
- Update to latest git snapshot

* Sun Jul 14 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1.20190714git284cadb
- Update to latest git snapshot

* Wed Jun 12 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-1.20190612gitceb42e5
- Initial package
