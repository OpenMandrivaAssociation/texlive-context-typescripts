Name:		texlive-context-typescripts
Version:	60422
Release:	2
Summary:	Small modules to load various fonts for use in ConTeXt
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-typescripts
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/typescripts
%doc %{_texmfdistdir}/doc/context/third/typescripts

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
