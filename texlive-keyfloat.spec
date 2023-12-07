Name:		texlive-keyfloat
Version:	65446
Release:	1
Summary:	Provides a key/value interface for generating floats
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyfloat
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyfloat.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyfloat.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyfloat.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The keyfloat package provides a key/value user interface for
quickly creating figures with a single image each, figures with
arbitrary contents, tables, subfloats, rows of floats, floats
located [H]ere, floats in the [M]argin, and floats with text
[W]rapped around them. Key/value combinations may specify a
caption and label, a width proportional to \linewidth, a fixed
width and/or height, rotation, scaling, a tight or loose frame,
an \arraystretch, a continued float, additional supplemental
text, and an artist/author's name with automatic index entry.
When used with the tocdata package, the name also appears in
the List of Figures. Floats may be placed into a row
environment, and are typeset to fit within the given number of
columns, continuing to the next row if necessary. Nested
sub-rows may be used to generate layouts such as two small
figures placed vertically next to one larger figure. Subfloats
are supported by two environments.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/keyfloat
%{_texmfdistdir}/tex/latex/keyfloat
%doc %{_texmfdistdir}/doc/latex/keyfloat

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
