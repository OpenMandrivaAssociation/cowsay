Summary:	Configurable talking cow
Name:		cowsay
Version:	3.8.4
Release:	1
License:	Artistic and GPL
Group:		Toys
URL:		https://github.com/cowsay-org/cowsay
Source0:	https://github.com/cowsay-org/cowsay/archive/v%{version}/%{name}-%{version}.tar.gz
Source9:	duck.cow
Source10:	apt.cow
Source11:	calvin.cow
Source12:	cock.cow
Source13:	small-duck.cow
Source14:	gnu.cow
Source15:	sodomized-sheep.cow
Source16:	suse.cow
Source17:	shark.cow
Source18:	girafe.cow
Source19:	phaco.cow
Source20:	pumpkin.cow
Source21:	kenny.cow
Patch0:		%{name}-3.8.4-makefile.patch
Patch1:		%{name}-3.8.4-elephant-in-snake.cow.patch
Patch2:		%{name}-3.8.4-luke-koala.cow.patch
#Patch3:		%{name}-3.8.4-mech-and-cow.cow.patch
BuildArch:	noarch

%description
Funny program to create ASCII images like cows, sheeps and much more.

%files
%license LICENSE.txt
%doc CHANGELOG.md README README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

#-----------------------------------------------------------------------

%prep
%autosetup -p1
perl -pi -e 's|%BANGPERL%|!%{_bindir}/perl|' cowsay
perl -pi -e 's|%PREFIX%|%{_prefix}|' cowsay cowsay.1


%build
# nothing to do here

%install
%make_install prefix=%{_prefix}
#install -d -m 755 %{buildroot}%{_bindir}
#install -m 755 cowsay %{buildroot}%{_bindir}
#(cd %{buildroot}%{_bindir} && ln -s cowsay cowthink)

#install -d -m 755 %{buildroot}%{_mandir}/man1
#install -m 644 cowsay.1 %{buildroot}%{_mandir}/man1
#(cd %{buildroot}%{_mandir}/man1 && ln -s cowsay.1 cowthink.1)

#install -d -m 755 %{buildroot}%{_datadir}/cows
#install -m 644 cows/* %{buildroot}%{_datadir}/cows
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE11} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE12} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE13} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE14} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE15} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE16} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE17} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE18} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE19} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE20} %{buildroot}%{_datadir}/%{name}/cows
install -m 644 %{SOURCE21} %{buildroot}%{_datadir}/%{name}/cows

%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.03-20mdv2011.0
+ Revision: 610166
- rebuild

* Thu Jan 21 2010 Pascal Terjan <pterjan@mandriva.org> 3.03-19mdv2010.1
+ Revision: 494625
- Restore nice duck and rename Debian one to small-duck.cow

* Fri Dec 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-18mdv2010.1
+ Revision: 476342
- fix [censored for sake of younger audience] cow

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 3.03-17mdv2010.0
+ Revision: 437131
- rebuild

* Wed Feb 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-16mdv2009.1
+ Revision: 337593
- keep bash completion in its own package

* Tue Dec 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-15mdv2009.1
+ Revision: 318024
- fix broken cow file
- add new cows from Debian package (#46560)
- uncompress additional sources

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 3.03-14mdv2009.0
+ Revision: 243695
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.03-12mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-12mdv2008.0
+ Revision: 67055
- rebuild


* Fri Jun 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-11mdv2007.0
- %%mkrel
- rpmbuildupdate aware

* Sat Jun 04 2005 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-10mdk 
- fix man page (fix #16291)

* Sat Jul 17 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.03-9mdk 
- hurry businesman compliant (aka two new wonderful cows)

* Sun Jul 11 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.03-8mdk 
- apologies to the girafes (with one only f)

* Sat Jun 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 3.03-7mdk 
- #mandrakefr compliant (aka four new additional cows)

* Thu Aug 21 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 3.03-6mdk
- save.the.world patch

