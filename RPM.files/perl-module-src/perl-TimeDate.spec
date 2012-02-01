Name: perl-TimeDate
Version: 1.16
Release: 4
Packager: Julian Field <mailscanner@ecs.soton.ac.uk>
Summary: TimeDate Perl module
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=TimeDate
BuildRoot: %{_tmppath}/%{name}-root
Buildarch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: TimeDate-1.16.tar.gz

%description
TimeDate Perl module
%prep
%setup -q -n TimeDate-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install DESTDIR=$RPM_BUILD_ROOT

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.gz" | \
	grep -v "\.packlist" > TimeDate-%{version}-filelist
if [ "$(cat TimeDate-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f TimeDate-%{version}-filelist
%defattr(-,root,root)

%changelog
* Thu Oct 10 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
