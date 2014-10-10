%define upstream_name    HTML-Display
%define upstream_version 0.40

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.40
Release:	2

Summary:	Use an OLE object to display HTML
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/HTML-Display-0.40.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTML::TokeParser::Simple)
BuildRequires:	perl(LWP)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(URI::URL)
BuildRequires:	perl-parent
BuildArch:	noarch

%description
This module abstracts the task of displaying HTML to the user. The
displaying is done by launching a browser and navigating it to either a
temporary file with the HTML stored in it, or, if possible, by pushing the
HTML directly into the browser window.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/HTML


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.390.0-1mdv2010.0
+ Revision: 402139
- rebuild using %%perl_convert_version

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2009.1
+ Revision: 333472
- import perl-HTML-Display


* Sun Jan 25 2009 cpan2dist 0.39-1mdv
- initial mdv release, generated with cpan2dist


