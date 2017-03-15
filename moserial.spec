Summary:	Serial terminal
Summary(pl.UTF-8):	Terminal szeregowy
Name:		moserial
Version:	3.0.11
Release:	1
License:	GPL v3+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/moserial/3.0/%{name}-%{version}.tar.xz
# Source0-md5:	2d8af3b524464f148b438162a8eac0be
URL:		https://wiki.gnome.org/moserial
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.12
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.12.0
Requires:	gtk+3 >= 3.0.0
Requires:	hicolor-icon-theme
Suggests:	lrzsz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A serial terminal optimized for logging and file capture.

%description -l pl.UTF-8
Terminal szeregowy zoptymalizowany pod kątem nagrywania i
przechwytywania plików.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/moserial
%{_datadir}/appdata/moserial.appdata.xml
%{_desktopdir}/moserial.desktop
%{_iconsdir}/hicolor/48x48/apps/moserial.png
%{_mandir}/man1/moserial.1*
