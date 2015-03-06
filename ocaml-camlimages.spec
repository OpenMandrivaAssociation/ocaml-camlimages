#empty-debuginfo-package
%define debug_package %{nil}
%define base_name camlimages

Summary:	Image processing library for Objective Caml
Name:		ocaml-%{base_name}
Version:	4.1.0
Release:	7
License:	LGPLv2+
Group:		Development/OCaml
Url:		http://cristal.inria.fr/camlimages/eng.html
Source0:	https://bitbucket.org/camlspotter/camlimages/get/%{version}.tar.gz
# This file isn't published any more (that I could find).
# It's probably dated but at least should provide some info on how to
# use the library.
Source1:	camlimages-2.2.0-htmlref.tar.gz
# https://bitbucket.org/camlspotter/camlimages/issue/9
Patch0:		ocaml-camlimages-4.1.0-exifcheck.patch
Patch1:		ocaml-camlimages-4.1.0-ocaml3.patch
Patch2:		ocaml-camlimages-4.1.0-giflib51.patch

BuildRequires:	chrpath
BuildRequires:	ghostscript
BuildRequires:	ocaml
BuildRequires:	ocaml-autoconf
BuildRequires:	ocaml-omake
BuildRequires:	ocaml-x11
BuildRequires:	giflib-devel
BuildRequires:	jpeg-devel
BuildRequires:	libgs-devel
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gdk-2.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(zlib)
Requires:	ghostscript
Requires:	ocaml-x11

%description
This is an image processing library, which provides some basic
functions of image processing and loading/saving various image file
formats. In addition the library can handle huge images that cannot be
(or can hardly be) stored into the memory (the library automatically
creates swap files and escapes them to reduce the memory usage).

%files
%doc README License.txt
%{_libdir}/ocaml/camlimages
%exclude %{_libdir}/ocaml/camlimages/*.a
%exclude %{_libdir}/ocaml/camlimages/*.cmxa
%exclude %{_libdir}/ocaml/camlimages/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for camlimages
Group:		Development/OCaml
Requires:	%{name} = %{EVRD}

%description devel
The camlimages-devel package provides libraries and headers for
developing applications using camlimages

Includes documentation provided by ocamldoc

%files devel
%doc htmlref
%{_libdir}/ocaml/camlimages/*.a
%{_libdir}/ocaml/camlimages/*.cmxa
%{_libdir}/ocaml/camlimages/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n camlspotter-camlimages-668faa3494fe
%setup -q -T -D -a 1 -n camlspotter-camlimages-668faa3494fe
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
omake CFLAGS="%{optflags}"

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
omake install

mkdir -p %{buildroot}%{_datadir}/doc/ocaml-camlimages
cp -pr License.txt htmlref %{buildroot}%{_datadir}/doc/ocaml-camlimages

