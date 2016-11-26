#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Importer
%include	/usr/lib/rpm/macros.perl
Summary:	Importer - Alternative but compatible interface to modules that export symbols
Summary(pl.UTF-8):	Importer - alternatywny, ale kompatybilny interfejs do modułów eksportujących symbole
Name:		perl-Importer
Version:	0.024
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/E/EX/EXODIST/Importer-%{version}.tar.gz
# Source0-md5:	2d29c79e65e221105a23e28c239b688f
URL:		http://search.cpan.org/dist/Importer/
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.98
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

%description -l pl.UTF-8
Ten moduł działa jako warstwa między Exporterem a modułami
pobierającymi wyeksportowane symbole. Jest zgodny co do możliwości z
Exporterem, zawiera też trochę dodatków. Można go użyć do importowania
symboli od dowolnego eksportera zgodnego ze specyfikacją Exportera.
Moduły eksportujące nie muszą wykorzystywać ani dziedziczyć z modułu
Exporter, muszą tylko ustawić @EXPORT i/lub inne zmienne.

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
%doc Changes README.md
%{perl_vendorlib}/Importer.pm
%{_mandir}/man3/Importer.3pm*
