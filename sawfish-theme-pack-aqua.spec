Summary:	A "pack" of aqua themes for Sawfish
Summary(pl):	Zestaw motywów aqua dla Sawfisha
Name:		sawfish-theme-pack-aqua
Version:	1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://download.freshmeat.net/themes/aquaesque/aquaesque-0.25.2.tar.gz
# Source0-md5:	0e776fe79b36be4ddf611953ca9bf093
Source1:	http://download.freshmeat.net/themes/aquaos/aquaos-0.%{version}9.tar.gz
# Source1-md5:	2f14cc0387140a1cf12f1980e0ebbebc
Source2:	http://download.freshmeat.net/themes/aquaos2/aquaos2-0.%{version}9.tar.gz
# Source2-md5:	ab9ccc933af1cd1d7770739eb10c4f0e
Source3:	http://download.freshmeat.net/themes/aquaz/aquaz-0.%{version}9.tar.gz
# Source3-md5:	de9c383411669a330391a2d6181dfdf0
Source4:	http://download.freshmeat.net/themes/sawtechaqua/sawtechaqua-0.28.tar.gz
# Source4-md5:	b4525ad57803ccf0ab0a7abefaa95315
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pack of themes for Sawfish:
- aquaesque
- aquaos
- aquaos2
- aquaz
- sawtechaqua

%description -l pl
Paczka z nastêpuj±cymi motywami dla Sawfisha:
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
install -d $RPM_BUILD_ROOT%{_datadir}/sawfish/themes

mv -f {Aquaesque,AquaOS,AquaOS2,AquaZ,SawTech-Aqua} \
	$RPM_BUILD_ROOT%{_datadir}/sawfish/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/*
