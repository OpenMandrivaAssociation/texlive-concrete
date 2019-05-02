# revision 15878
# category Package
# catalog-ctan /fonts/concrete
# catalog-date 2006-12-08 15:31:01 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-concrete
Version:	20190228
Release:	1
Summary:	Concrete Roman fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/concrete
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/concrete.doc.tar.xz
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
%{_texmfdistdir}/fonts/source/public/concrete/cccsc10.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccmi10.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccmic9.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr10.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr5.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr6.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr7.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr8.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccr9.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccsl10.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccsl9.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccslc9.mf
%{_texmfdistdir}/fonts/source/public/concrete/ccti10.mf
%{_texmfdistdir}/fonts/source/public/concrete/odigs.mf
%{_texmfdistdir}/fonts/tfm/public/concrete/cccsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccmic9.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr10.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr5.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr6.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr7.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr8.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccr9.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccslc9.tfm
%{_texmfdistdir}/fonts/tfm/public/concrete/ccti10.tfm
%doc %{_texmfdistdir}/doc/fonts/concrete/CATALOGUE
%doc %{_texmfdistdir}/doc/fonts/concrete/Makefile
%doc %{_texmfdistdir}/doc/fonts/concrete/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061208-2
+ Revision: 750422
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061208-1
+ Revision: 718118
- texlive-concrete
- texlive-concrete
- texlive-concrete
- texlive-concrete

