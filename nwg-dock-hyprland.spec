Name:           nwg-dock-hyprland
Version:        0.3.2
Release:        1
Summary:        Hyprland application dock
License:        MIT
Group:          NWG/Hyrpland
URL:            https://github.com/nwg-piotr/nwg-dock-hyprland
Source0:        https://github.com/nwg-piotr/nwg-dock-hyprland/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  go >= 1.22
BuildRequires:  compiler(go-compiler)
BuildRequires:  zstd
BuildRequires:  pkgconfig(gtk-layer-shell-0)

%description
Configurable (w/ command line arguments and css) dock, written in Go, aimed
exclusively at the Hyprland Wayland compositor. It features pinned buttons,
client buttons and the launcher button.

%prep
%autosetup -p1 -a1

%build
## Note build takes around 10 minutes, so be patient as there is no output!
go build \
   -mod=vendor \
   -buildmode=pie

%install
install -d -m 0755 %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 config/style.css %{buildroot}%{_datadir}/%{name}/style.css

%files
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/style.css
