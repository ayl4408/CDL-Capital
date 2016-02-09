<?php
session_start(); // Starting Session

//$rows = 0;
$error=''; // Variable To Store Error Message

if (isset($_POST['submit'])) {

	if (empty($_POST['username']) || empty($_POST['password'])) {
		
		$error = "Empty Username or Password is invalid";
	
	}else{

		// Define $username and $password
		$username=$_POST['username'];
		$password=$_POST['password'];

		// Establishing Connection with Server by passing server_name, user_id and password as a parameter

		$dbhost = "localhost";
		$dbuser = "root";
		$dbpass = "mmGr2016";
		$dbname = "cdlcapital";
		$connection = mysql_connect($dbhost, $dbuser, $dbpass) or die("Unable to connect to MySQL");

		// To protect MySQL injection for Security purpose
		
		//Selecting Database
		$db = mysql_select_db($dbname, $connection);

		// SQL query to fetch information of registerd users and finds user match.
		$query = mysql_query("select * from users where password='$password' AND login='$username'");
		$rows = mysql_num_rows($query);

		if ($rows == 1) {
			//$error = " Correct Username or Password is invalid";
			$_SESSION['login_user']=$username; // Initializing Session
			header("location: profile.php"); // Redirecting To Other Page
		} else {
			$error = " Wrong Username or Password is invalid";
		}

		mysql_close($connection); // Closing Connection
	}
}
?>
