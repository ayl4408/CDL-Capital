<?php include 'header.php';?>

<head>
  <link rel="stylesheet" type="text/css" href="stylesheet.css">
</head>

<form action="front_router.php" method="post" >
	Upload via Yahoo:
	<br/>
    <label>Company Name: </label><input type="text" name="comp_name" /><br/>
    <label>Start Date:</label><input type="text" name="start_date" /><br/>
    <label>End Date: </label><input type="text" name="end_date" /><br/>
    <label></label><input type="submit" value="Upload" name="upload2"><br/>
</form>

<br/>
<br/>

<form action="router/front_router.php" method="post" enctype="multipart/form-data">
    Upload via CSV File:
    <br/>
    <label></label><input type="file" name="file" id="file"><br/>
    <label></label><input type="submit" value="Upload" name="upload"><br/>
</form>



