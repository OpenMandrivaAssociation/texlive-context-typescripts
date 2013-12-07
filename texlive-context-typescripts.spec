# revision 25411
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-typescripts
# catalog-date 2012-02-16 15:23:58 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-context-typescripts
Version:	20120216
Release:	3
Summary:	Small modules to load various fonts for use in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-typescripts
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
The package provides files offering interfaces to 33 publicly
available fonts (or collections of fonts from the same
foundry); each is available in a .mkii and a .mkiv version.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/typescripts/type-adobe.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-adobe.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-aller.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-aller.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-anivers.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-anivers.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-audimat.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-audimat.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-axel.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-axel.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-azuro.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-azuro.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-calluna.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-calluna.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-charissil.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-charissil.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-charter.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-charter.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-delicious.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-delicious.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-diavlo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-diavlo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-droid.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-droid.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-ernestine.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fertigo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-fertigo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fontin.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-fontin.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-goudysans.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-goudysans.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-junicode.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-junicode.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-justus.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-justus.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-kaffeesatz.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-kaffeesatz.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-kontrapunkt.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-kontrapunkt.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-liberation.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-liberation.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-luxi.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-luxi.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-miso.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-miso.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-museo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-museo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-office.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-pigiarniq.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-pigiarniq.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-sabon.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-sabon.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-tallys.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-tallys.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-tuffy.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-tuffy.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-ubuntu.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-ubuntu.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-uqammaq.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-uqammaq.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-vera.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-vera.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-verajja.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-verajja.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-vollkorn.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-vollkorn.mkiv
%doc %{_texmfdistdir}/doc/context/third/typescripts/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120216-1
+ Revision: 779435
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-4
+ Revision: 750531
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-3
+ Revision: 745203
- texlive-context-typescripts

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 739714
- texlive-context-typescripts

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 729673
- texlive-context-typescripts

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110115-1
+ Revision: 718145
- texlive-context-typescripts
- texlive-context-typescripts
- texlive-context-typescripts
- texlive-context-typescripts

