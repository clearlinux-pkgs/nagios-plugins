#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nagios-plugins
Version  : 2.2.1
Release  : 3
URL      : https://nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz
Source0  : https://nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz
Summary  : Host/service/network monitoring program plugins for Nagios
Group    : Development/Tools
License  : GPL-3.0
Requires: nagios-plugins-bin
Requires: nagios-plugins-locales
BuildRequires : gnutls-dev
BuildRequires : mariadb-dev
BuildRequires : openssl-dev
BuildRequires : procps-ng

%description
Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.

%package bin
Summary: bin components for the nagios-plugins package.
Group: Binaries

%description bin
bin components for the nagios-plugins package.


%package extras
Summary: extras components for the nagios-plugins package.
Group: Default

%description extras
extras components for the nagios-plugins package.


%package locales
Summary: locales components for the nagios-plugins package.
Group: Default

%description locales
locales components for the nagios-plugins package.


%prep
%setup -q -n nagios-plugins-2.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507408667
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1507408667
rm -rf %{buildroot}
%make_install
%find_lang nagios-plugins

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/libexec/check_breeze
%exclude /usr/libexec/check_disk_smb
%exclude /usr/libexec/check_file_age
%exclude /usr/libexec/check_flexlm
%exclude /usr/libexec/check_ifoperstatus
%exclude /usr/libexec/check_ifstatus
%exclude /usr/libexec/check_ircd
%exclude /usr/libexec/check_mailq
%exclude /usr/libexec/check_rpc
%exclude /usr/libexec/check_wave
/usr/libexec/check_apt
/usr/libexec/check_clamd
/usr/libexec/check_cluster
/usr/libexec/check_disk
/usr/libexec/check_dummy
/usr/libexec/check_ftp
/usr/libexec/check_http
/usr/libexec/check_ide_smart
/usr/libexec/check_imap
/usr/libexec/check_jabber
/usr/libexec/check_load
/usr/libexec/check_log
/usr/libexec/check_mrtg
/usr/libexec/check_mrtgtraf
/usr/libexec/check_nagios
/usr/libexec/check_nntp
/usr/libexec/check_nntps
/usr/libexec/check_nt
/usr/libexec/check_ntp
/usr/libexec/check_ntp_peer
/usr/libexec/check_ntp_time
/usr/libexec/check_nwstat
/usr/libexec/check_oracle
/usr/libexec/check_overcr
/usr/libexec/check_ping
/usr/libexec/check_pop
/usr/libexec/check_procs
/usr/libexec/check_real
/usr/libexec/check_sensors
/usr/libexec/check_simap
/usr/libexec/check_smtp
/usr/libexec/check_spop
/usr/libexec/check_ssh
/usr/libexec/check_ssmtp
/usr/libexec/check_swap
/usr/libexec/check_tcp
/usr/libexec/check_time
/usr/libexec/check_udp
/usr/libexec/check_ups
/usr/libexec/check_uptime
/usr/libexec/check_users
/usr/libexec/negate
/usr/libexec/urlize
/usr/libexec/utils.pm
/usr/libexec/utils.sh

%files extras
%defattr(-,root,root,-)
/usr/libexec/check_breeze
/usr/libexec/check_disk_smb
/usr/libexec/check_file_age
/usr/libexec/check_flexlm
/usr/libexec/check_ifoperstatus
/usr/libexec/check_ifstatus
/usr/libexec/check_ircd
/usr/libexec/check_mailq
/usr/libexec/check_rpc
/usr/libexec/check_wave

%files locales -f nagios-plugins.lang
%defattr(-,root,root,-)

