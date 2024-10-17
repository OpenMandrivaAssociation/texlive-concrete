Name:		texlive-concrete
Version:	57963
Release:	2
Summary:	Concrete Roman fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/concrete
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Concrete Roman fonts, designed by Donald E. Knuth, originally
for use with Euler mathematics fonts. Alternative mathematics
fonts, based on the concrete 'parameter set' are available as
the concmath fonts bundle. LaTeX support is offered by the
beton, concmath and ccfonts packages. T1- and TS1-encoded
versions of the fonts are available in the ecc bundle, and
Adobe Type 1 versions of the ecc fonts are part of the cm-super
bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/concrete
%{_texmfdistdir}/fonts/tfm/public/concrete
%doc %{_texmfdistdir}/doc/fonts/concrete

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
