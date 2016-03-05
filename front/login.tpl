<!DOCTYPE html>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <title>CDL Capital</title>
  </head>

  <body>
    <div class="container">
      <div class="jumbotron">
	<h1>CDL Capital</h1>
	<br/>
      </div>
      <div id="main">
	<div class="row">
	  <div id="login">
	    <form action=${validate_login_link}$ method="post" class="form-horizontal" role="form">
	      <div class="form-group">
		<label class="control-label col-sm-1" for="username"></label>
		<div class="col-sm-3">
		  <input class="form-control" id="username" name="username" placeholder="Username" type="text" required>
		</div>
	      </div>
	      <div class="form-group">
		<label class="control-label col-sm-1" for="password"></label>
		<div class="col-sm-3">
		  <input class="form-control" id="password" name="password" placeholder="********" type="password" required>
		</div>
	      </div>
	      <div class="form-group">
		<div class="col-sm-offset-1 col-sm-1">
		  <input class="form-control" name="submit" type="submit" value="Submit">
		</div>
	      </div>
	    </form>
	  </div>
	</div>
      </div>
    </div>
  </body>
</html>
