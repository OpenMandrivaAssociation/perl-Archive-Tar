%define	modname	Archive-Tar
%define	modver	1.90

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	4

Summary:	Perl module for manipulation of tar archives
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/%{modname}-%{modver}.tar.gz

BuildRequires:	perl(IO::Compress::Bzip2)	>= 2.012
BuildRequires:	perl(Test::Pod)			>= 0.95
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl-devel

BuildArch:	noarch

Requires:	perl(IO::Compress::Bzip2)	>= 2.012
Requires:	perl(IO::Uncompress::Bunzip2)	>= 2.012

%description
Archive::Tar provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation. If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or gzipped
tar files.

An object of class Archive::Tar represents a .tar(.gz) archive full of files
and things.

%prep
%setup -q -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Archive/Tar
%{perl_vendorlib}/Archive/Tar.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.900.0-3
- add back man pages
- new version

* Thu Dec 20 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.820.0-5
- rebuild against perl-5.16.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-4
+ Revision: 765054
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-3
+ Revision: 763478
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 1.820.0-2
+ Revision: 763233
- force it
- rebuild

* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.820.0-1
+ Revision: 759458
- version update 1.82

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.680.0-2
+ Revision: 667027
- mass rebuild

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.680.0-1mdv2011.0
+ Revision: 572217
- update to 1.68

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.660.0-1mdv2011.0
+ Revision: 561552
- update to 1.66

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.640.0-1mdv2011.0
+ Revision: 552255
- update to 1.64

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2010.1
+ Revision: 539069
- update to 1.60

* Thu Feb 18 2010 Jérôme Quelin <jquelin@mandriva.org> 1.580.0-1mdv2010.1
+ Revision: 507584
- update to 1.58

* Fri Feb 05 2010 Jérôme Quelin <jquelin@mandriva.org> 1.560.0-1mdv2010.1
+ Revision: 501139
- update to 1.56

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.540.0-1mdv2010.0
+ Revision: 437211
- update to 1.54

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.520.0-1mdv2010.0
+ Revision: 395039
- update to 1.52
- using %%perl_convert_version
- fixed license field
- update to new version 1.48

* Mon Feb 16 2009 Oden Eriksson <oeriksson@mandriva.com> 1.44-2mdv2009.1
+ Revision: 340844
- fix deps

* Mon Feb 16 2009 Oden Eriksson <oeriksson@mandriva.com> 1.44-1mdv2009.1
+ Revision: 340829
- 1.44

* Tue Jan 20 2009 Oden Eriksson <oeriksson@mandriva.com> 1.40-1mdv2009.1
+ Revision: 331735
- 1.40 (fixes CVE-2007-4829)

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.38-2mdv2009.0
+ Revision: 223500
- rebuild

* Fri Dec 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.38-1mdv2008.1
+ Revision: 138800
- update to new version 1.38

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2008.1
+ Revision: 97365
- update to new version 1.36

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.34-1mdv2008.0
+ Revision: 69203
- update to new version 1.34

* Sat Jul 07 2007 Funda Wang <fwang@mandriva.org> 1.32-1mdv2008.0
+ Revision: 49308
- New version

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdv2008.0
+ Revision: 46311
- update to new version 1.31


* Mon Aug 07 2006 rafael
+ 08/07/06 16:01:42 (53994)
1.30

* Mon Aug 07 2006 rafael
+ 08/07/06 15:59:57 (53993)
Import perl-Archive-Tar

* Mon Mar 06 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.29-1mdk
- 1.29

* Wed Jan 25 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.28-1mdk
- 1.28

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdk
- New release 1.26
- drop patch0 (merged upstream)
- fix directory ownership
- spec cleanup

* Mon Aug 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.25-1mdk
- 1.25
- Doesn't depend on IO::String anymore
- Install ptardiff(1) utility (patch0, upstream bug:)

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.24-1mdk
- 1.24

* Tue Dec 07 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.23-1mdk
- 1.23

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.22-1mdk
- 1.22

* Tue Nov 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.21-1mdk
- 1.21
- fix buildrequires

* Tue Jun 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10-1mdk
- 1.10
- cosmetics

* Mon May 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.09-1mdk
- 1.09
- the ptar utility returns.

* Wed Apr 21 2004 Michael Scherer <misc@mandrake.org> 1.08-1mdk 
- 1.08
- [DIRM]
- rpmbuildupdate aware

* Thu Aug 28 2003 FranÃ§ois Pons <fpons@mandrakesoft.com> 1.05-1mdk
- removed ptar no more available.
- 1.05.
