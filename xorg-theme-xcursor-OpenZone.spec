Summary:	X11 mouse theme
Name:		xorg-theme-xcursor-OpenZone
Version:	1.2.3
Release:	1
License:	X11
Group:		Themes
Source0:	http://gnome-look.org/CONTENT/content-files/111343-OpenZone-%{version}.tar.xz
# Source0-md5:	4dae968cbd525072664ef7a4fc7c4154
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenZone xcursor themes.

%prep
%setup -qn OpenZone

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

tar -xf OpenZone_Black-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_Black_Slim-1.2.3.tar.xz  -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_Fire-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_Fire_Slim-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_Ice-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_Ice_Slim-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_White-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}
tar -xf OpenZone_White_Slim-1.2.3.tar.xz -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING
%{_iconsdir}/OpenZone_Black
%{_iconsdir}/OpenZone_Black_Slim
%{_iconsdir}/OpenZone_Fire
%{_iconsdir}/OpenZone_Fire_Slim
%{_iconsdir}/OpenZone_Ice
%{_iconsdir}/OpenZone_Ice_Slim
%{_iconsdir}/OpenZone_White
%{_iconsdir}/OpenZone_White_Slim

