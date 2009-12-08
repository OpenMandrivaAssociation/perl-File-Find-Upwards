%define upstream_name    File-Find-Upwards
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Look for a file in the current directory and upwards
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Attribute::Memoize)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Provides a function that can find a file in the current or a parent
directory.

* file_find_upwards()

  Takes a filename and looks for the file in the current directory. If
  there is no such file, it traverses up the directory hierarchy until it
  finds the file or until it reaches the topmost directory. If the file is
  found, the full path to the file is returned. If the file is not found,
  undef is returned.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


