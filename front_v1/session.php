
<?php
// Establishing Connection with Server by passing server_name, user_id and password as a parameter
session_start();// Starting Session

$dbhost = "localhost";
$dbuser = "root";
$dbpass = "mmGr2016";
$dbname = "cdlcapital";
$connection = mysql_connect($dbhost, $dbuser, $dbpass) or die("Unable to connect to MySQL");



// Selecting Database
$db = mysql_select_db($dbname, $connection);

// Storing Session
$user_check=$_SESSION['login_user'];

$ses_sql=mysql_query("select * from users where login='$user_check'");
$row = mysql_num_rows($ses_sql);
//$login_session =$row['login'];

mysql_close($connection); // Closing Connection

//if(!isset($login_session)){
if($row != 1){
	header('Location: login_view.php'); // Redirecting To Home Page
}


?>
