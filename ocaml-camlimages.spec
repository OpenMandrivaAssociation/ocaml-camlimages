%define base_name	camlimages
%define name		ocaml-%{base_name}
%define version		2.20
%define release		%mkrel 9

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
BuildRequires:	ocaml-lablgtk-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description 
CamlImages is an image processing library for Objective Caml

%package devel
Summary:	Image processing library for Objective Caml
Group:		Development/Other
Provides:	%{base_name} = %{version}-%{release}
Obsoletes:	%{name}
Provides:	%{name}

%description devel
CamlImages is an image processing library for Objective Caml

%prep
%setup -q -n %{base_name}-2.2
%patch -p0

%build
#%configure --disable-rpath
./configure
make all opt

%install
rm -rf %{buildroot}
make LIBDIR=%{buildroot}%{_libdir}/ocaml/%{base_name} install

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc Announce CHANGES INSTALL LICENSE README
%{_libdir}/ocaml/%{base_name}


