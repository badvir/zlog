Name:           zlog
Version:        1.2.12
Release:        1
Summary:        zlog logger framework

License:        LGPL
URL:            http://hardysimpson.github.io/zlog/
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  gcc make

%define package_name    %{name}-%{version}


%description
AIRTAME Web Service is powering the setup page.


%prep
#cp -a %_sourcedir/%{package_name}.tar.gz %_builddir/
#cd %_builddir
#tar xvf %{package_name}.tar.gz
#rm %{package_name}.tar.gz

%setup -q


%build
#cd %{package_name}
./make

%install
install -d '%{buildroot}/usr/include'
install -d '%{buildroot}/usr/lib64'
cp src/zlog.h '%{buildroot}/usr/include/zlog.h'
cp build/Linux/lib/libzlog.a '%{buildroot}/usr/lib64/libzlog.a'
cp build/Linux/lib/libzlog.so.1.2.12 '%{buildroot}/usr/lib64/libzlog.so.1.2'
ln -sf /usr/lib64/libzlog.so.1.2 '%{buildroot}/usr/lib64/libzlog.so.1'
ln -sf /usr/lib64/libzlog.so.1.2 '%{buildroot}/usr/lib64/libzlog.so'

%clean

%files
/usr/include/zlog.h
/usr/lib64/libzlog.a
/usr/lib64/libzlog.so
/usr/lib64/libzlog.so.1
/usr/lib64/libzlog.so.1.2
