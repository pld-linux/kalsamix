%define		_rel		beta2
Summary:	An ALSA mixer for KDE
Summary(pl.UTF-8):	Mikser ALSA dla KDE
Name:		kalsamix
Version:	1.0.0
Release:	0.%{_rel}.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/kalsamix/%{name}-%{version}%{_rel}.tar.gz
# Source0-md5:	f81ba7798ce887b92c3a07ecfc879df4
Patch0:		%{name}-desktop.patch
URL:		http://kamix.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A KDE mixer application for KDE 3 and ALSA, just to provide some
support for what official kmix lacks.

%description -l pl.UTF-8
Mikser dżwięku dla KDE 3 i ALSY, posiadający możliwości, w które kmix
jest ubogi.

%prep
%setup -q -n %{name}-%{version}%{_rel}
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--disable-rpath \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop
