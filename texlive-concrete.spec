%global tl_name concrete
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Concrete Roman fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/concrete
License:	knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Concrete Roman fonts, designed by Donald E. Knuth, originally for use
with Euler mathematics fonts. Alternative mathematics fonts, based on
the concrete 'parameter set' are available as the concmath fonts bundle.
LaTeX support is offered by the beton, concmath and ccfonts packages.
T1- and TS1-encoded versions of the fonts are available in the ecc
bundle, and Adobe Type 1 versions of the ecc fonts are part of the cm-
super bundle.

