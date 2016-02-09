<?php
session_start();
if(session_destroy()) // Destroying All Sessions
{
header("Location: login_view.php"); // Redirecting To Home Page
}
?>