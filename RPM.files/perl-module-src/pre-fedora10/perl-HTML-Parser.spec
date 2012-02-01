Name: perl-HTML-Parser
Version: 3.56
Release: 1
Packager: Julian Field <mailscanner@ecs.soton.ac.uk>
Summary: HTML-Parser Perl module
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=HTML%3a%3aParser
BuildRoot: %{_tmppath}/%{name}-root
Source0: HTML-Parser-3.56.tar.gz

%description
HTML-Parser Perl module
%prep
%setup -q -n HTML-Parser-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
#make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > HTML-Parser-%{version}-filelist
if [ "$(cat HTML-Parser-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f HTML-Parser-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
