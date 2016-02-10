<?php

	$c=$_POST["c"];
    $dbhost = "sql1.njit.edu";
    $dbuser = "kc343";
    $dbpass = "njitdb123";
    $dbname = "kc343";
    $dbh = mysql_connect($dbhost, $dbuser, $dbpass) or die("Unable to connect to MySQL");
    $selected = mysql_select_db($dbname,$dbh);

    //$index = mysql_query("SELECT * from {$c}");
    $index = mysql_query("SELECT * FROM googl WHERE id={$c}");
    //$index = mysql_query("SELECT * FROM {$index_temp} ORDER BY ID DESC")
    $num_rows = mysql_num_rows($index); 



    //$index_array = array

    echo json_encode($json_2d);


    mysql_close($dbh);


?>