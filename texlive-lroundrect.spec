Name:		texlive-lroundrect
Version:	39804
Release:	2
Summary:	LaTeX macros for utilizing the roundrect MetaPost routines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lroundrect
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides ways to use the extremely
configurable rounded rectangles of the roundrect MetaPost
package with LaTeX. It is chiefly useful for examples, but also
has macros for particular types of boxes which are useful on
their own.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/lroundrect
%{_texmfdistdir}/tex/latex/lroundrect
%doc %{_texmfdistdir}/doc/latex/lroundrect

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
