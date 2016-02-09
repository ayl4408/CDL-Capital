<?php
	include('session.php');
?>

<!DOCTYPE html>
<html>

<head>
	<script type="text/javascript" src="jquery/jquery-1.9.1.min.js"></script>
  	<script type="text/javascript" src="jquery/jquery.autocomplete.min.js"></script>
	<meta charset="utf-8">
  	<meta name="viewport" content="width=device-width, initial-scale=1">
  	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  	<script type="text/javascript" src="https://www.google.com/jsapi"></script>
  	<script src="https://code.highcharts.com/highcharts.js"></script>
</head>
 	<body>
		<div class="container">
			<div class="jumbotron">
		      	<h1>CDL Capital</h1>
		      	<h5>Welcome to your profile, <?php echo $user_check; ?></h5>
</br>	
				<ul class="nav nav-pills">
				   	<li class="active"><a href="http://cdl.ddns.net:4098/CDLCapital/Front/profile.php">My Profile</a></li>
			      	<li><a href="http://cdl.ddns.net:4098/CDLCapital/Front/home.php">Analysis</a></li>
			      	<li><a href="http://cdl.ddns.net:4098/CDLCapital/Front/logout.php">Logout</a></li>
				</ul>
			</div>

			<ul class ="nav nav-tabs">
			    <li class="active"><a data-toggle="tab" href="#home">Portfolio</a></li>
			    <li><a data-toggle="tab" href="#menu1">Transactions</a></li>
			</ul>

			<div class="tab-content">
				<div id="menu1" class="tab-pane fade">
</br>
</br>
					<div class="row">
						<form id="deposit_form" class="form-horizontal" role="form">
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
									<h3>Deposit</h3>
								</div>
							</div>
							<div class="form-group">
							    <label class="control-label col-sm-1" for="amount">Amount:</label>
                        		<div class="col-sm-3">
								    <input class="form-control" type="number" min="0" id="amount" type="text" name="amount" />
								</div>
							</div>
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
								    <input class="form-control" id="deposit" type="button" value="Submit" onclick="Deposit();"/>
								</div>
							</div>
						</form>
						<div id="deposit_status"></div>
					</div>

					<div class="row">
						<form id="buy_form" class="form-horizontal" role="form">
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
									<h3>Buy</h3>
								</div>
							</div>
							<div class="form-group">
								<label class="control-label col-sm-1" for="company_name_buy">Company</label>
								<div class="col-sm-3">
									<input class="form-control"  id="company_name_buy" type="text" name="company_name" />
								</div>
							</div>
							<div class="form-group">
								<label class="control-label col-sm-1" for="volume_buy">Volume:</label>
								<div class="col-sm-3">
									<input class="form-control"  type="number" min="0" id="volume_buy" type="number" name="volume_buy" />
								</div>
							</div>
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
									<input class="form-control" id="Buy" type="button" value="Submit" onclick="buy();"/> 
								</div>
							</div>
						</form>
						<div id="outputbox"><p id="outputcontent"></p></div>
						<div id="buy_status"></div>
					</div>

					<div class="row">
						<form class="sell_form form-horizontal" id="sell_form" role="form">
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
									<h3>Sell</h3>
								</div>
							</div>
							<div class="form-group">
								<div class="col-sm-offset-1 col-sm-1">
						        	<select id="company_name_sell" name="company_name_sell"></select>
						        </div>
					    	</div>
					        <div class="form-group">
						        <label class="control-label col-sm-1" for="volume_sell">Volume:</label>
						        <div class="col-sm-3">
						        	<input class="form-control" type="number" min="0" id="volume_sell" type="number" name="volume_sell" />
						    	</div>
					    	</div>
					    	<div class="form-group">
					    		<div class="col-sm-offset-1 col-sm-1">
									<input class="form-control" id="Sell" type="button" value="Submit" onclick="sell();"/> 
								</div>
							</div>
				        </form>	
					</div>
</br>
</br>
</br>
				</div>
<br/>
<br/>
				<div id="home" class="tab-pane fade in active">			
					<div class="row">
			      		<div class="col-sm-4" sidenav>
			      			<h4>Portfolio Information</h4>
			      			<table class="table table-hover user_table">
		                        <thead>
							        <tr>
							            <th>Total Portfolio</th>
							            <th>Available Funds</th>
							            <th>Total Stock Values</th>
							            <th>Total Profit</th>
							            <th>Total Deposited</th>
							        </tr>
		                        </thead>
						    </table>
<br>
<br>
				      		<div id="user_information"></div>

			      			<h4>Owned Stocks</h4>
			      			<table class="table table-hover owned_stocks_table">
						  		<thead>  
		                            <tr>
							            <th>Stock</th>
							            <th>Shares</th>
							            <th>Current Price</th>
							            <th>Total Worth</th>
							            <th>Profit</th>
					        		</tr>
		                        </thead>
					    	</table>
<br>
<br>
			      			<div id="owned_stocks_information"></div>      		
			      		</div>
			      		<div class="col-sm-8">
							<div id="piechart" style="width: 900px; height: 500px;"></div>
						</div>
			      	</div>
<br>
<br>	      	
			      	<div class="row">
						<h4>Recent Transactions</h4>
			      			<table class="table table-hover transaction_table">
			      			<thead><tr>
					            <th>Transaction Date </th>
					            <th>Transaction Type</th>
					            <th>Stock</th>
					            <th>Price</th>
					            <th>Volume</th>
					            <th>Total Price</th>
					        </tr></thead>
					    	</table>
<br>
<br>
			      			<div id="transaction_information"></div>
					</div>
				</div>
<br/>
<br/>
		</div>
	</div>
<script type="text/javascript">

	var intervalId = null;
	/*var clientTime = new Date();
	offset =  -5.0;
	utc = clientTime.getTime()+(clientTime.getTimezoneOffset() * 60000);
	serverDate = new Date(utc + (3600000*offset));
	console.log(serverDate);
	hour = clientTime.getHours();
	min = clientTime.getMinutes();
	sec = clientTime.getSeconds();
	console.log("current Time is " + hour + ":" + min + ":" + sec);*/
	var get_stock_symbol="get_stock_symbol";
    var stock_symbol_result = $.ajax({
        type: 'POST',
        url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
        data: 'get_stock_symbol='+ get_stock_symbol,
        dataType: "json",
        async: false}).responseText;
    var stock_symbol_parsed=JSON.parse(stock_symbol_result);
      //console.log(stock_symbol_parsed);

    $(function(){
        var data = stock_symbol_parsed;
        //console.log(data);
        
        // setup autocomplete function pulling from currencies[] array
        $('#company_name_buy').autocomplete({
          lookup: data,
          onSelect: function (suggestion) {
            var thehtml = '<strong>Stock:</strong> ' + suggestion.data + ' <br> <strong>Symbol:</strong> ' + suggestion.value;
            //$('#outputcontent').html(thehtml);
          }
        })
      })
	window.onload = start;


	function start()
	{
		generate_sell_drop_down();
		update_profile_information();
		intervalId = setInterval(update_profile_information, 60000);
	}

	function generate_sell_drop_down()
	{
		var user_name='<?php echo $user_check; ?>';
		var generate_sell_drop_down="generate_sell_drop_down";
		var generate_sell_drop_down_parsed = [];

		var generate_sell_drop_down_result = $.ajax({
			type: 'POST',
			url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
			data: 'user_name='+ user_name + '&sell_companies_list='+ generate_sell_drop_down,
			dataType: "json",
			async: false}).responseText;

		generate_sell_drop_down_parsed=JSON.parse(generate_sell_drop_down_result);
		//console.log(generate_sell_drop_down_parsed);
		$('#company_name_sell').empty();
		$('<option value="Companies"> Companies </option>').appendTo('#company_name_sell');
	    for(var field in generate_sell_drop_down_parsed) {
	         $('<option value="'+ generate_sell_drop_down_parsed[field]['stock'] +'">' + generate_sell_drop_down_parsed[field]['stock'] + '</option>').appendTo('#company_name_sell');
	    }
	}

	function update_profile_information()
	{
		var user_name='<?php echo $user_check; ?>';
		var update_profile="update_profile";

		var update_profile_result = $.ajax({
			type: 'POST',
			url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
			data: 'user_name='+ user_name + '&update_profile='+ update_profile,
			dataType: "json",
			async: false}).responseText;

		var update_profile_result_parsed=JSON.parse(update_profile_result);
		console.log(update_profile_result_parsed);
		load_profile_information();
	}

	function load_profile_information()
	{
		var user_name='<?php echo $user_check; ?>';
		var profile_information="profile_information";
		profile_info_result = $.ajax({
			type: 'POST',
			url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
			data: 'user_name='+ user_name + '&profile_information='+ profile_information,
			dataType: "json",
			async: false}).responseText;

		var profile_info_result_parsed=JSON.parse(profile_info_result);
		//console.log(profile_info_result_parsed[2]);
		table_generate_users(profile_info_result_parsed[0]);
		table_generate_transactions(profile_info_result_parsed[1]);
		table_generate_owned_stocks(profile_info_result_parsed[2]);
		drawChart();
	}

	function table_generate_users (json_array) 
	{
	        var $formrow = '<tbody><tr><td>'+json_array[0]['total_portfolio']+'</td><td>'+json_array[0]['available_funds']+'</td><td>'+json_array[0]['total_stock_values']+'</td><td>'+json_array[0]['profit']+'</td><td>'+json_array[0]['total_deposited']+'</td></tr></tbody>';
	        $('.user_table tr td').remove();
	        $('.user_table').append($formrow);
	} 

	function table_generate_transactions (json_array) 
	{
			var length=json_array.length;
			$('.transaction_table tr td').remove();

			for (var i=0; i<length; i++){
	        	var $formrow = '<tbody><tr><td>'+json_array[i]['trans_date']+'</td><td>'+json_array[i]['trans_type']+'</td><td>'+json_array[i]['stock']+'</td><td>'+json_array[i]['price']+'</td><td>' + json_array[i]['volume']+'</td><td>' + json_array[i]['total_price']+'</td></tr></tbody>';
	        	$('.transaction_table').append($formrow);
	    	}
	}

	function table_generate_owned_stocks (json_array) 
	{
			var length=json_array.length;
			$('.owned_stocks_table tr td').remove();

			for (var i=0; i<length; i++)
			{
	        	var $formrow = '<tbody><tr><td>'+json_array[i]['stock']+'</td><td>'+json_array[i]['current_shares']+'</td><td>'+json_array[i]['current_price']+'</td><td>'+json_array[i]['total_worth']+'</td><td>'+json_array[i]['profit']+'</td></tr></tbody>';
	        	$('.owned_stocks_table').append($formrow);
	        }
	} 

	function Deposit()
	{
		var user_name='<?php echo $user_check; ?>';
		var amount=document.getElementById('amount');

		if(amount.value > 0)
		{
			var deposit = "deposit";
			var deposit_result = $.ajax({
				type: 'POST',
				url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
				data: 'user_name='+ user_name + '&amount='+ amount.value + '&deposit='+ deposit,
				dataType: "datastring",
				async: false}).responseText;
				
	     	document.getElementById('deposit_status').innerHTML = deposit_result;
	     	load_profile_information();
     	}
     	document.getElementById("deposit_form").reset();
    }
	
	function buy()
	{
		var user_name='<?php echo $user_check; ?>';
		var company_name=document.getElementById('company_name_buy');
		var volume=document.getElementById('volume_buy');

		if(volume.value > 0)
		{
			var buy = "buy";
			var buy_result = $.ajax({
				type: 'POST',
				url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
				data: 'user_name='+ user_name + '&company_name='+ company_name.value + '&volume='+ volume.value  + '&buy='+ buy,
				dataType: "json",
				async: false}).responseText;

			//console.log(buy_result);
		    //load_profile_information();
		    update_profile_information();
  		}
  		generate_sell_drop_down();
  		document.getElementById("buy_form").reset();
    }
    
	function sell()
	{
		var user_name='<?php echo $user_check; ?>';
		var company_name=company_name_sell.value;
		var volume=document.getElementById('volume_sell');
		var sell_result;

		if(volume.value > 0)
		{
			var sell = "sell";
			sell_result = $.ajax({
				type: 'POST',
				url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
				data: 'user_name='+ user_name + '&company_name='+ company_name + '&volume='+ volume.value  + '&sell='+ sell,
				dataType: "json",
				async: false}).responseText;
	    		
			update_profile_information();
		}
		console.log(sell_result);
		generate_sell_drop_down();
		document.getElementById("sell_form").reset();
    };
</script>

<script type="text/javascript">

    var flag=true;
    var counter=0;
    function drawChart() 
    {
    	counter=counter+1;

    	if(counter>1)
    	{
    		flag=false;
    	}

    	var user_name='<?php echo $user_check; ?>';
		var portfolio_distribution ="portfolio_distribution";

    	var portfolio_distribution = $.ajax({
			type: 'POST',
			url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
			data: 'user_name='+ user_name + '&portfolio_distribution='+ portfolio_distribution,
			dataType: "json",
			async: false}).responseText;
		
		portfolio_distribution_parsed=JSON.parse(portfolio_distribution);
    	
    	$(function () {
	    	$('#piechart').highcharts({
	        chart: {
	            plotBackgroundColor: null,
	            plotBorderWidth: null,
	            plotShadow: false,
	            type: 'pie'
	        },
	        title: {
	            text: 'Portfolio Distribution'
	        },
	        tooltip: {
	            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
	        },
	        plotOptions: {                 
	             pie: {
	             	animation: flag,
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
	        },
	        series: [{
	            name: 'Stocks',
	            colorByPoint: true,
	            data: portfolio_distribution_parsed
	        }]
	    });
	});
    }
</script>

	</body>
</html>