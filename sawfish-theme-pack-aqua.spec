Summary:	A "pack" of aqua themes for Sawfish
Summary(pl):	Zestaw tematów aqua dla Sawfish'a
Name:		sawfish-theme-pack-aqua
Version:	1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://download.freshmeat.net/themes/aquaesque/aquaesque-0.25.2.tar.gz
Source1:	http://download.freshmeat.net/themes/aquaos/aquaos-0.%{version}9.tar.gz
Source2:	http://download.freshmeat.net/themes/aquaos2/aquaos2-0.%{version}9.tar.gz
Source3:	http://download.freshmeat.net/themes/aquaz/aquaz-0.%{version}9.tar.gz
Source4:	http://download.freshmeat.net/themes/sawtechaqua/sawtechaqua-0.28.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A pack of themes for Sawfish:
- aquaesque
- aquaos
- aquaos2
- aquaz
- sawtechaqua

%description -l pl
Paczka z nastêpuj±cymi tematami dla Sawfisha:
- aquaesque
- aquaos
- aquaos2
- aquaz
- sawtechaqua

%prep
%setup -q -c -b 0 -b 1 -b 2 -b 3 -b 4

rm -rf AquaOS2/.xvpics AquaZ/.xvpics

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/

mv -f {Aquaesque,AquaOS,AquaOS2,AquaZ,SawTech-Aqua} \
	$RPM_BUILD_ROOT%{_datadir}/sawfish/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/*
