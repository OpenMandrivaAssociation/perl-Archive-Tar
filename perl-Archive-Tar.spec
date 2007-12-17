%define	module	Archive-Tar
%define	name	perl-%{module}
%define version 1.36
%define release	%mkrel 1

Summary:	Perl module for manipulation of tar archives
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/K/KA/KANE/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module for manipulation of tar archives.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Archive
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*


