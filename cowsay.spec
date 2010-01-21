%define name    cowsay
%define version 3.03
%define release %mkrel 19

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Configurable talking cow
License:    Artistic and GPL
Group:      Toys
URL:        http://www.nog.net/~tony/warez/cowsay.shtml
Source0:    http://www.nog.net/~tony/warez/%{name}-%{version}.tar.bz2
Source9:    duck.cow
Source10:   apt.cow
Source11:   calvin.cow
Source12:   cock.cow
Source13:   small-duck.cow
Source14:   gnu.cow
Source15:   sodomized-sheep.cow
Source16:   suse.cow
Source17:   shark.cow
Source18:   girafe.cow
Source19:   phaco.cow
Source20:   pumpkin.cow
Source21:   kenny.cow
Patch0:		%{name}.save.the.world.patch
Patch1:		%{name}-3.03-elephant-in-snake.cow.patch
Patch2:		%{name}-3.03-luke-koala.cow.patch
Patch3:		%{name}-3.03-mech-and-cow.cow.patch
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Funny program to create ASCII images like cows, sheeps and much more.

%prep
%setup -q
perl -pi -e 's|%BANGPERL%|!%{_bindir}/perl|' cowsay
perl -pi -e 's|%PREFIX%|%{_prefix}|' cowsay cowsay.1
%patch0
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 cowsay %{buildroot}%{_bindir}
(cd %{buildroot}%{_bindir} && ln -s cowsay cowthink)

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 cowsay.1 %{buildroot}%{_mandir}/man1
(cd %{buildroot}%{_mandir}/man1 && ln -s cowsay.1 cowthink.1)

install -d -m 755 %{buildroot}%{_datadir}/cows
install -m 644 cows/* %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE11} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE12} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE13} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE14} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE15} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE16} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE17} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE18} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE19} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE20} %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE21} %{buildroot}%{_datadir}/cows

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README INSTALL
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/cows

