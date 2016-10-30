#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Importer
%include	/usr/lib/rpm/macros.perl
Summary:	Importer - Alternative but compatible interface to modules that export symbols
Name:		perl-Importer
Version:	0.024
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EX/EXODIST/Importer-%{version}.tar.gz
# Source0-md5:	2d29c79e65e221105a23e28c239b688f
URL:		http://search.cpan.org/dist/Importer/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module acts as a layer between Exporter and modules which consume
exports. It is feature-compatible with Exporter, plus some much needed
extras. You can use this to import symbols from any exporter that
follows Exporters specification. The exporter modules themselves do
not need to use or inherit from the Exporter module, they just need to
set @EXPORT and/or other variables.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Importer.pm
%{_mandir}/man3/Importer.3pm*
