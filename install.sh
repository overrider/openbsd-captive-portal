#!/bin/sh

echo "IMPORTANT!!!"
echo "Running this may overwrite important configuration files"
echo "such as /etc/pf.conf /etc/dhcpd.conf /var/named/etc/named.conf"
echo "It is probably better to adjust and copy the config files manually"
echo "Either way, you want to read trough this script first and see what it does"

echo -n "Hit enter to continue or CTRL+C to cancel"
read GOAHEAD

echo "Copying Files, wait a few moments..."

cp etc/rc.conf.local /etc/
cp etc/pf.conf /etc/
touch /var/db/whitelist
cp etc/dhcpd.conf /etc/
cp etc/hostname.athn0 /etc/
cp etc/hostname.alc0 /etc/
cp etc/mygate /etc/
cp etc/sysctl.conf /etc/
cp etc/rc.d/obsdcp /etc/rc.d/
cp etc/resolv.conf /etc/

cp usr/local/bin/obsdcp /usr/local/bin/

cp var/www/conf/Obsdcp_config.pm /var/www/conf/
cp var/www/conf/httpd.conf /var/www/conf/
cp var/www/conf/obsdcp_allow.txt /var/www/conf/
cp var/www/conf/obsdcp_queue.txt /var/www/conf/

cp var/www/htdocs/* /var/www/htdocs/
cp var/www/htdocs/.htaccess /var/www/htdocs/

cp var/named/etc/named.conf /var/named/etc/
cp var/named/etc/rndc.conf /var/named/etc/
cp var/named/etc/rndc.key /var/named/etc/

if [[ ! -e /var/www/usr ]]; then
	mkdir /var/www/usr
fi

if [[ ! -e /var/www/usr/bin ]]; then
	mkdir /var/www/usr/bin
fi

if [[ ! -e /var/www/usr/lib ]]; then
	mkdir /var/www/usr/lib
fi

if [[ ! -e /var/www/usr/libdata ]]; then
	mkdir /var/www/usr/libdata
fi

if [[ ! -e /var/www/usr/libexec ]]; then
	mkdir /var/www/usr/libexec
fi

cp /usr/bin/perl /var/www/usr/bin/
cp /usr/lib/libperl.so.* /var/www/usr/lib/
cp /usr/lib/libm.so.* /var/www/usr/lib/
cp /usr/lib/libutil.so.* /var/www/usr/lib/
cp /usr/lib/libc.so.* /var/www/usr/lib/
cp /usr/libexec/ld.so /var/www/usr/libexec/
cp -r /usr/libdata/perl5 /var/www/usr/libdata/

echo "----"
echo "Done"
echo "Now adjust the configuration files to your needs and reboot"
echo "Make sure the /etc/hostname.if files are correct and match your interfaces"
echo "Make sure the right route is set in /etc/mygate"
echo "Make sure /etc/dhcpd.conf is per your liking"
