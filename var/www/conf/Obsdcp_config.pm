#!/usr/bin/perl

package Obsdcp_config;
use strict;
use warnings;
use Exporter;

our @ISA = 'Exporter';
our @EXPORT = qw(%accounts $queue $whitelist_timeout $whitelist $allow $purge_interval $expiry_time);

our %accounts;
$accounts{'guest1'} = "guest1";
$accounts{'guest2'} = "guest2";

if($> == 0){
	our $queue = "/var/www/conf/obsdcp_queue.txt";
} else {
	our $queue = "/conf/obsdcp_queue.txt";
}

# Time to allow authenticated client access before
# removing him from the list again and asking for
# re-auth. Default is 300 seconds = 5 minutes :-)
our $expiry_time = 300;

# How many times the process_obsdcp_queue program 
# checks for expired IPs and rewrites the allow
# table. Lets make it every two minutes.
our $purge_interval = 120;

our $allow = "/var/www/conf/obsdcp_allow.txt";

our $whitelist = "/var/db/whitelist";
