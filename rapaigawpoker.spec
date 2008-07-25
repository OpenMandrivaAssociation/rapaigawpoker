%define name    rapaigawpoker
%define version 1.1
%define release %mkrel 7

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
License:        GPLv2+
BuildRequires:  SDL-devel SDL_ttf-devel automake1.4

%description
A Poker-like card game, played against a dealer at a casino.
It is played with 52 card deck and a joker. You have a more detailed
help on rules in the game itself.
It has an English (default) and a Serbian language option.


%prep 
%setup -q

%build 
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# Menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_bindir}/%{name}
Icon=%{_datadir}/%{name}/Ikone/48x48/%{name}.png
Categories=CardGame;Game;
Name=%{title}
Comment=%{longtitle}
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc README NEWS COPYING AUTHORS THANKS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
