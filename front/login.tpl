<!DOCTYPE html>
<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <title>CDL Capital</title>

    <style>
      body {
      padding-top: 40px;
      padding-bottom: 40px;
      background-color: #eee;
      }

      .form-signin {
      max-width: 330px;
      padding: 15px;
      margin: 0 auto;
      }
      .form-signin .form-signin-heading,
      .form-signin .checkbox {
      margin-bottom: 10px;
      }
      .form-signin .checkbox {
      font-weight: normal;
      }
      .form-signin .form-control {
      position: relative;
      height: auto;
      -webkit-box-sizing: border-box;
      -moz-box-sizing: border-box;
      box-sizing: border-box;
      padding: 10px;
      font-size: 16px;
      }
      .form-signin .form-control:focus {
      z-index: 2;
      }
      .form-signin input[type="text"] {
      margin-bottom: -1px;
      border-bottom-right-radius: 0;
      border-bottom-left-radius: 0;
      }
      .form-signin input[type="password"] {
      margin-bottom: 10px;
      border-top-left-radius: 0;
      border-top-right-radius: 0;
      }

      #headerImg{
         max-width:100%;
      }
    </style>
    

  </head>

  <body>
    <div class="container">
      <center><img id="headerImg" src="http://cliparts.co/cliparts/rcn/Kxo/rcnKxonLi.png"/></center>
      <form class="form-signin" action="${validate_login_link}$" method="POST">
	<h3 class="form-signin-heading"><b><u>CDL Capital</u></b><br>Sign-In</h3>
	<label for="inputEmail" class="sr-only">Email address</label>
	<input type="text" id="username" name="username" class="form-control" placeholder="Username" required autofocus>
	<label for="inputPassword" class="sr-only">Password</label>
	<input type="password" id="password" name="password" class="form-control" placeholder="Password" required>
	<div class="checkbox">
	  <label>
	    <input type="checkbox" value="remember-me"> Remember me
	  </label>
	</div>
	<button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>
  </body>
</html>
