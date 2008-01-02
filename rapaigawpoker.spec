%define name    rapaigawpoker
%define version 1.1
%define release %mkrel 4

%define section Amusement/Cards
%define title RA Pai Gaw Poker
%define longtitle Poker-like card game

Name:           %{name}
Summary:        %{longtitle}
Version:        %{version}
Release:        %{release}
Source0:        http://relja.narod.ru/download/games/%{name}-%{version}.tar.bz2 
URL:            http://relja.narod.ru/english/download.html
Group:          Games/Cards
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot 
License:        GPL
BuildRequires:  SDL-devel SDL_ttf-devel
Requires:       SDL SDL_ttf

%description
A Poker-like card game, played against a dealer at a casino.
It is played with 52 card deck and a joker. You have a more detailed
help on rules in the game itself.
It has an English (default) and a Serbian language option.


%prep 
%setup -q

%build 
%configure 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Meni
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%name): \
command="%{_bindir}/%{name}" \
needs="X11" \
icon="%{_datadir}/%{name}/Ikone/48x48/%{name}.png" \
section="%{section}" \
title="%{title}" \
longtitle="%{longtitle}"
EOF

%post
%{update_menus}

%postun
%{clean_menus}


%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc README NEWS COPYING AUTHORS THANKS

%{_bindir}/%{name}
%{_datadir}/%{name}/Dugme/*
%{_datadir}/%{name}/Font/*
%{_datadir}/%{name}/Help/*
%{_datadir}/%{name}/Ikone/*
%{_datadir}/%{name}/Karte/*
%{_datadir}/%{name}/Zetoni/*
%{_menudir}/%{name}



