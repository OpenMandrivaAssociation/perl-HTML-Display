%define upstream_name    HTML-Display
%define upstream_version 0.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Use an OLE object to display HTML
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTML::TokeParser::Simple)
BuildRequires: perl(LWP)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(URI::URL)
BuildRequires: perl-parent
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module abstracts the task of displaying HTML to the user. The
displaying is done by launching a browser and navigating it to either a
temporary file with the HTML stored in it, or, if possible, by pushing the
HTML directly into the browser window.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/HTML
