%define name    cowsay
%define version 3.03
%define release %mkrel 12

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Configurable talking cow
License:        Artistic and GPL
Group:          Toys
URL:            http://www.nog.net/~tony/warez/cowsay.shtml
Source0:        http://www.nog.net/~tony/warez/%{name}-%{version}.tar.bz2
Source1:        %{name}.completion.bz2
Source2:        %{name}-more-cows.tar.bz2
Patch0:		%{name}.save.the.world.patch
BuildArch:      noarch

%description
Funny program to create ASCII images like cows, sheeps and much more.

%prep
%setup -q
%setup -q -T -D -a 2
bzcat %{SOURCE1} > cowsay.completion
perl -pi -e 's|%BANGPERL%|!%{_bindir}/perl|' cowsay
perl -pi -e 's|%PREFIX%|%{_prefix}|' cowsay cowsay.1
%patch0

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

install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 cowsay.completion %{buildroot}%{_sysconfdir}/bash_completion.d/cowsay

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README INSTALL
%config(noreplace) %{_sysconfdir}/bash_completion.d/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/cows

