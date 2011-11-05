# revision 23167
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-typescripts
# catalog-date 2011-01-15 19:42:27 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-context-typescripts
Version:	20110115
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3

%description
Supported font families are Accanthis; Adobe Minion, Myriad,
Sabon and Warnock; Aller; Apostrophic Labs Amerika, Ashby,
Charrington, Covington, Day Roman, Devroye, Florence Sans,
Komikazba, Komikaze, Labrit, Lady Copra, Lady Ice, Steinem,
Street Corner, Usenet, Youthanasia and Zebrra; Arkandis
Accanthis, Baskervald, Berenis, Gillius, Ikarius, Irianis,
Libris, Mekanus, Romande, Switzera, Tribun, Universalis and
Verana; Asana math; Baar Metanoia, Philos and Sophia; Bera
Serif, Sans and Mono; Calluna; Charis SIL; Charter; Computer
Modern Unicode; DejaVu; Droid; Exljbris Anivers, Delicious,
Diavlo, Fertigo, Fontin, Museo and Tallys; Fontsite Bergamo and
Carto Gothic; GFS Ambrosia, Artemisia, Bodoni, Didot, Elpis,
Eustace, Fleischman, Jackson, Neohellenic, Nicefore and
Theokritos; Junicode; Justus; Kontrapunkt; Leftist; Liberation;
Linux Libertine; Luxi; MgOpen Canonica, Moderna and Modata;
Miso; Nichtlustig NICHTLUSDICK and NICHTLUSDUENN; Pigiarniq;
Richtype Francesca and Klara; Sabon; Samba; Smeltery Audimat,
Geronto, Megalopolis and Trottoir; Tuffy; Uqammaq; Vera;
Verajja; Vista Cambria, Candara, Calibri, Consolas, Constantia
and Corbel; and Vollkorn.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post
    %_texmf_mtxrun_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
	%_texmf_mtxrun_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/third/typescripts/type-adobe.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-adobe.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-aller.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-aller.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-anivers.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-anivers.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-apostrophiclab.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-apostrophiclab.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-apostrophiclab.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-arkandis.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-arkandis.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-baar.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-baar.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-bera.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-bera.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-calluna.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-calluna.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-charissil.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-charissil.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-charter.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-charter.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-cmu.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-cmu.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-dejavu.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-dejavu.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-delicious.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-delicious.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-diavlo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-diavlo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-droid.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-droid.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-exljbris.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-exljbris.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fertigo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-fertigo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fontin.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-fontin.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fontsite.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-fontsite.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-fontsite.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-gfs.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-gfs.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-gfs.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-junicode.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-justus.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-kaffeesatz.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-kaffeesatz.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-kontrapunkt.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-leftist.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-liberation.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-liberation.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-linuxlibertine.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-linuxlibertine.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-linuxlibertine.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-luxi.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-luxi.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-mgopen.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-mgopen.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-mgopen.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-miso.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-museo.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-museo.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-nichtlustig.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-optical.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-pigiarniq.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-pigiarniq.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-richtype.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-richtype.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-richtype.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-sabon.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-sabon.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-samba.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-smeltery.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-smeltery.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-smeltery.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-tallys.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-tallys.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-tuffy.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-tuffy.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-uqammaq.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-vera.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-vera.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-vera.tex
%{_texmfdistdir}/tex/context/third/typescripts/type-verajja.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-verajja.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-vista.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-vista.mkiv
%{_texmfdistdir}/tex/context/third/typescripts/type-vollkorn.mkii
%{_texmfdistdir}/tex/context/third/typescripts/type-vollkorn.mkiv
%doc %{_texmfdistdir}/doc/context/third/typescripts/README
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
