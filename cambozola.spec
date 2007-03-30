Summary:	content/multipart streamed JPEG viewer
Summary(pl.UTF-8):	Przeglądarka obrazów JPEG content/multipart
Name:		cambozola
Version:	0.68
Release:	1
License:	GPL v2
Group:		Libraries
# http://www.charliemouse.com/code/cambozola/
Source0:	http://www.charliemouse.com/code/cambozola/%{name}-%{version}.tar.gz
# Source0-md5:	e4fac8b6ee94c9075b14bb95be4f860b
URL:		http://www.charliemouse.com/code/cambozola/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cambozola is a very simple (cheesey!) viewer for multipart JPEG
streams that are often pumped out by a streaming webcam server,
sending over multiple images per second. Netscape will display and
refresh these automatically, but Internet Explorer and other browsers
do not - they will only display the first image.

%description -l pl.UTF-8
Cambozola jest prostą przeglądarką dla wieloczęściowych strumieni
JPEG, często udostępnianych przez kamery WWW, wysyłające wiele obrazów
na sekundę. Netscape wyświetli i będzie odświeżać podgląd
automatycznie, ale Internet Explorer i inne przeglądarki nie -
wyświetlą tylko pierwszy obrazek.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -D dist/cambozola.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
