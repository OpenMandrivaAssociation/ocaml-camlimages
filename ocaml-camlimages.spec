%define base_name	camlimages
%define name		ocaml-%{base_name}
%define version		2.20
%define release		%mkrel 13

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	Image processing library for Objective Caml
Group:		Development/Other
URL:		http://pauillac.inria.fr/camlimages
Source:		ftp://ftp.inria.fr/INRIA/caml-light/bazar-ocaml/%{base_name}-2.2.0.tar.bz2
Patch:		ocaml-camlimages-uint16.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-lablgl-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
CamlImages is an image processing library for Objective Caml

%package devel
Summary:	Image processing library for Objective Caml
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-lablgl-devel
Requires:	ocaml-lablgtk2-devel

%description devel
CamlImages is an image processing library for Objective Caml

%prep
%setup -q -n %{base_name}-2.2
%patch -p0

%build
%configure2_5x \
    --with-lablgl=%{_libdir}/ocaml/lablgl \
    --with-lablgtk2=%{_libdir}/ocaml/lablgtk2
make all opt

%install
rm -rf %{buildroot}
make LIBDIR=%{buildroot}/%{_libdir}/ocaml/%{base_name} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Announce CHANGES INSTALL LICENSE README
%dir %{_libdir}/ocaml/%{base_name}
%{_libdir}/ocaml/%{base_name}/*.cmi
%{_libdir}/ocaml/%{base_name}/*.cma
%{_libdir}/ocaml/%{base_name}/*.so

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/%{base_name}/*
%exclude %{_libdir}/ocaml/%{base_name}/*.cmi
%exclude %{_libdir}/ocaml/%{base_name}/*.cma
%exclude %{_libdir}/ocaml/%{base_name}/*.so
