#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	PostScript
%define		pnam	Simple
Summary:	PostScript::Simple - produce PostScript files from Perl
Summary(pl):	PostScript::Simple - tworzenie plików PostScript z poziomu Perla
Name:		perl-PostScript-Simple
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	836f74f3fab6631faeb92a8310b57140
URL:		http://search.cpan.org/dist/PostScript-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostScript::Simple allows you to have a simple method of writing
PostScript files from Perl. It has several graphics primitives that
allow lines, circles, polygons and boxes to be drawn. Text can be
added to the page using standard PostScript fonts.

%description -l pl
PostScript::Simple udostêpnia prosty sposób tworzenia plików
PostScript z poziomu Perla. Ma ró¿ne graficzne prymitywy pozwalaj±ce
na rysowanie linii, okrêgów, wielok±tów i pude³ek. Mo¿na dodawaæ do
stron tekst przy u¿yciu standardowych fontów postscriptowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/PostScript/Simple.pm
%dir %{perl_vendorlib}/PostScript/Simple
%{perl_vendorlib}/PostScript/Simple/EPS.pm
%{_mandir}/man3/*
