%define base_name	camlimages
%define name		ocaml-%{base_name}
%define version		2.20
%define release		%mkrel 11

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
    --with-lablgl=%{ocaml_sitelib}/lablgl \
    --with-lablgtk2=%{ocaml_sitelib}/lablgtk2
make all opt

%install
rm -rf %{buildroot}
make LIBDIR=%{buildroot}%{ocaml_sitelib}/%{base_name} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Announce CHANGES INSTALL LICENSE README
%dir %{ocaml_sitelib}/%{base_name}
%{ocaml_sitelib}/%{base_name}/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/%{base_name}/*
%exclude %{ocaml_sitelib}/%{base_name}/*.cmi
