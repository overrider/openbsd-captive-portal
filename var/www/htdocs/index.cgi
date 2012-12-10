#!/usr/bin/perl

use CGI;
use CGI::Carp 'fatalsToBrowser';
use strict;
use warnings;

use lib '/conf/';
use Obsdcp_config;

my $query = new CGI;

if(! -e -w $queue){
	die("$queue is not writeable or does not exist");
}

my $ip_address = $ENV{'REMOTE_ADDR'};

if ($query->param("submit")) {
	process_form (); 
} else {
	display_form ();
}


sub process_form {
if(validate_form()){
	print $query->header();
	enable_access();
	print <<END_HTML;
<html>
	<head>
		<title>Captive Portal</title>
		<link rel="stylesheet" type="text/css" href="/main.css" />
		<meta http-equiv="Pragma" content="no-cache" />
		<meta http-equiv="Expires" content="-1" />
		<meta http-equiv="CACHE-CONTROL" content="NO-CACHE" />
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
	</head>
	<body>
		<div id="wrapper">
			<div id="header">
				<h2>Access granted!</h2>
			</div>
			<div id="content">
				<p>Your access will expire in $expiry_time seconds.</p>

				<h3>A few useful Links</h3>
				<a href="http://www.duckduckgo.com/">DuckDuckGo</a><br />
				<a href="http://www.openbsd.org/">OpenBSD</a><br />
				<a href="http://www.bsdguides.org/">BSDGuides</a><br />
			</div>
			<div id="footer">
				<img src="banner.png" />
			</div>
			<div id="push"></div>
		</div>
		<div id="credit">
			<p>Powered by <a href="http://www.openbsd.org">OpenBSD</a></p>
		</div>
	</body>
</html>

END_HTML
}
}

sub enable_access {
	open FILE, ">>",$queue or die $!;
	print FILE "$ip_address\n";
	close FILE;
}

sub validate_form {
	my $username = $query->param("username");
	my $password = $query->param("password");

	my $error_message = "";

	$error_message .= "Please enter username<br />" if ( !$username);
	$error_message .= "Please enter password<br />" if ( !$password);

	if(!exists($accounts{$username}) || $accounts{$username} ne $password){
		$error_message .= "Authentication failed<br />";
	}

	if ( $error_message ) {
		$error_message = "<div id='error_msg'>" . $error_message . "</div>";
		display_form ($error_message);
		return 0;
	} else {
		return 1;
	}
}

sub display_form {
  print $query->header();
  my $error_message = shift;

  print <<END_HTML;
<html>
	<head>
		<title>Captive Portal</title>
		<link rel="stylesheet" type="text/css" href="/main.css" />
		<meta http-equiv="Pragma" content="no-cache" />
		<meta http-equiv="Expires" content="-1" />
		<meta http-equiv="CACHE-CONTROL" content="NO-CACHE" />
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
	</head>
	<body OnLoad="document.loginform.username.focus();">
		<div id="wrapper">
			<div id="header">
				<h2>Access restricted!</h2>
			</div>
			<div id="content">
				<p>Please authenticate yourself for Internet access.</p>
				<form name="loginform" action="" method="post">
					<input type="hidden" name="submit" value="Submit">
					<label>Username:</label>
					<input type="text" name="username" value="" tabindex="1" />
					<label>Password:</label>
					<input type="password" name="password" value="" tabindex="2" />
					<input type="submit" value="Submit" name="submit" class="submit" tabindex="3" />
					<p style="font-size: 0.8em;">By clicking Submit you agree to our Terms of Use</p>
					$error_message
				</form>   
			</div>
			<div id="footer">
				<img src="banner.png" />
			</div>
			<div id="push"></div>
		</div>
		<div id="credit">
			<p>Powered by <a href="http://www.openbsd.org">OpenBSD</a></p>
		</div>
	</body>
</html>
END_HTML
}
