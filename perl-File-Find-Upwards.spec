%define upstream_name    File-Find-Upwards
%define upstream_version 1.102030

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Look for a file in the current directory and upwards
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Attribute::Memoize)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.102.30-2mdv2011.0
+ Revision: 654961
- rebuild for updated spec-helper

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 1.102.30-1mdv2011.0
+ Revision: 561569
- update to 1.102030

* Sun Mar 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.860-1mdv2011.0
+ Revision: 528431
- update to 1.100860

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.1
+ Revision: 474656
- update to 0.04

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 444064
- import perl-File-Find-Upwards


* Thu Sep 17 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
