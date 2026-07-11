%global tl_name lroundrect
%global tl_revision 39804

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	LaTeX macros for utilizing the roundrect MetaPost routines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/lroundrect
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lroundrect.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package provides ways to use the extremely configurable
rounded rectangles of the roundrect MetaPost package with LaTeX. It is
chiefly useful for examples, but also has macros for particular types of
boxes which are useful on their own.

