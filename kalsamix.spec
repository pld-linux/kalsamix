Summary:	An ALSA mixer for KDE
Summary(pl):	Mikser ALSA dla KDE
Name:		kamix
Version:	0.6.5
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/kamix/%{name}-%{version}.tar.bz2
# Source0-md5:	d73930700aca9a81020db45c65002111
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

%description -l pl
Mikser d¿wiêku dla KDE 3 i ALSY, posiadaj±cy mo¿liwo¶ci, w które kmix
jest ubogi.

%prep
%setup -q -n %{name}
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

%files -f kamix.lang
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/kamix
%{_datadir}/apps/kamix
%{_iconsdir}/hicolor/*/*/*
%{_desktopdir}/*.desktop
