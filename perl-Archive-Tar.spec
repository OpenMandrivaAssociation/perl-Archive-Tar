%define	modname	Archive-Tar
%define	modver	1.90

Summary:	Perl module for manipulation of tar archives
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(IO::Compress::Bzip2) >= 2.012
BuildRequires:	perl(Test::Pod) >= 0.95
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl-devel
Requires:	perl(IO::Compress::Bzip2) >= 2.012
Requires:	perl(IO::Uncompress::Bunzip2) >= 2.012

%description
Archive::Tar provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation. If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or gzipped
tar files.

An object of class Archive::Tar represents a .tar(.gz) archive full of files
and things.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README
%{_bindir}/*
%{perl_vendorlib}/Archive/Tar
%{perl_vendorlib}/Archive/Tar.pm
%{_mandir}/man1/*
%{_mandir}/man3/*

