%define	upstream_name	 Archive-Tar
%define upstream_version 1.58

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Perl upstream_name for manipulation of tar archives
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(IO::Compress::Bzip2) >= 2.012
BuildRequires:	perl(Test::Pod) >= 0.95
BuildRequires:	perl(Text::Diff)
BuildRequires:	perl-devel

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(IO::Compress::Bzip2)     >= 2.012
Requires:	perl(IO::Uncompress::Bunzip2) >= 2.012

%description
Archive::Tar provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation. If you have the
IO::Zlib upstream_name installed, Archive::Tar will also support compressed or gzipped
tar files.

An object of class Archive::Tar represents a .tar(.gz) archive full of files
and things.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor -d
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}

%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Archive/Tar
%{perl_vendorlib}/Archive/Tar.pm
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*
