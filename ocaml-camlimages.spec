%define base_name	camlimages
%define name		ocaml-%{base_name}
%define version		3.0.2
%define release		%mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	Image processing library for Objective Caml
Group:		Development/Other
URL:		http://cristal.inria.fr/camlimages/eng.html
Source:		http://cristal.inria.fr/camlimages/%{base_name}-%{version}.tgz
Patch0: camlimages-3.0.2-display-module.patch 
# https://bugzilla.redhat.com/show_bug.cgi?id=528732
Patch2: camlimages-oversized-tiff-check-CVE-2009-3296.patch
Patch3: camlimages-3.0.2-ocaml-autoconf.patch
BuildRequires:  ocaml >= 3.10.1
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libxpm-devel
#BuildRequires:  ghostscript-devel
BuildRequires:  libgs-devel
BuildRequires:  freetype-devel
BuildRequires:  libungif-devel
BuildRequires:  libtiff-devel
BuildRequires:  ocaml-autoconf 
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
CamlImages is an image processing library for Objective Caml

%package devel
Summary:	Image processing library for Objective Caml
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-lablgtk2-devel

%description devel
CamlImages is an image processing library for Objective Caml

%prep
%setup -q -n %{base_name}-%{version}
%patch0 -p1
%patch2 -p1 -b .CVE-2009-3296
%patch3 -p1
aclocal -I .
automake
autoconf

# Gdk.Display submodule clashes with the Display module in
# the examples/liv directory, so rename it:
mv examples/liv/display.ml examples/liv/livdisplay.ml

%build
%configure2_5x \
    --without-lablgtk \
    --with-lablgtk2 \
    --with-lablgtk2-dir=%{_libdir}/ocaml/lablgtk2
make

%install
rm -rf %{buildroot}
make install ocamlsitelibdir=%{_libdir}/ocaml/camlimages DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL README
%dir %{_libdir}/ocaml/%{base_name}
%{_libdir}/ocaml/%{base_name}/META
%{_libdir}/ocaml/%{base_name}/*.cmi
%{_libdir}/ocaml/%{base_name}/*.cma
%{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(-,root,root)
%doc doc/*.{html,jpg}
%{_libdir}/ocaml/%{base_name}/*
%exclude %{_libdir}/ocaml/%{base_name}/META
%exclude %{_libdir}/ocaml/%{base_name}/*.cmi
%exclude %{_libdir}/ocaml/%{base_name}/*.cma
