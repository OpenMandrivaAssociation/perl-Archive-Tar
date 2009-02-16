%define	module	Archive-Tar

Summary:	Perl module for manipulation of tar archives
Name:		perl-%{module}
Version:	1.44
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Archive::Tar provides an object oriented mechanism for handling tar files. It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation. If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or gzipped
tar files.

An object of class Archive::Tar represents a .tar(.gz) archive full of files
and things.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
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
%{perl_vendorlib}/Archive
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*
