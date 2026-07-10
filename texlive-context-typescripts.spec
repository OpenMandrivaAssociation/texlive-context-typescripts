%global tl_name context-typescripts
%global tl_revision 76524

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Small modules to load various fonts for use in ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-typescripts
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-typescripts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides files offering interfaces to 33 publicly available
fonts (or collections of fonts from the same foundry); each is available
in a .mkii and a .mkiv version.

