%define base_name	camlimages
%define name		ocaml-%{base_name}
%define version		3.0.1
%define release		%mkrel 4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	Image processing library for Objective Caml
Group:		Development/Other
URL:		http://gallium.inria.fr/camlimages/
Source:		http://gallium.inria.fr/camlimages/%{base_name}-%{version}.tar.bz2
Patch0:         camlimages-3.0.1-display-module.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=509531#c4
Patch1:         camlimages-oversized-png-check-CVE-2009-2295.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=528732
Patch2:         camlimages-oversized-tiff-check-CVE-2009-3296.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}
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

# Gdk.Display submodule clashes with the Display module in
# the examples/liv directory, so rename it:
%patch0 -p1
mv examples/liv/display.ml examples/liv/livdisplay.ml

%patch1 -p1 -b .CVE-2009-2295
%patch2 -p1 -b .CVE-2009-3296

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
