%define module   HTML-Display
%define version    0.39
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Use an OLE object to display HTML
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTML/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(HTML::TokeParser::Simple)
BuildRequires: perl(LWP)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(URI::URL)
BuildRequires: perl-parent
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This module abstracts the task of displaying HTML to the user. The
displaying is done by launching a browser and navigating it to either a
temporary file with the HTML stored in it, or, if possible, by pushing the
HTML directly into the browser window.

%prep
%setup -q -n %{module}-%{version} 

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


