<!DOCTYPE html>
<html>

<head>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
    <!--<script type="text/javascript" src="jquery/jquery-1.9.1.min.js"></script>
        <script type="text/javascript" src="jquery/jquery.autocomplete.min.js"></script>
    -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://cdl.ddns.net:4098/mycss.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="//code.jquery.com/ui/1.11.4/themes/smoothness/jquery-ui.css">
    <script src="//code.jquery.com/jquery-1.10.2.js"></script>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script src="//code.jquery.com/ui/1.11.4/jquery-ui.js"></script>
    <script src="https://code.highcharts.com/highcharts.js"></script>

    <style>
        #algorithm_graph_dropdown_types_div{
            display:inline;
            float:left;    
        }

        #algorithm_graph_dropdown_lines_div{
            float:left;
            margin-left: 5px;
        }

    	#algorithms_menu select{
    		min-width:300px;
    		width:20%;
    		display:inline;
    	}

    	#header{
    		background: -webkit-linear-gradient(#F5F0E4, #E0D8C1);
    		background: -o-linear-gradient(#F5F0E4, #E0D8C1);
    		background: -moz-linear-gradient(#F5F0E4, #E0D8C1);
    		background: linear-gradient(#F5F0E4, #E0D8C1);

    		position:fixed;
    		width:100%;
    		height:50px;
    		z-index:1;
    		text-align:center;
    		color:black;

    	}

    	#logout{
    		float:right;
    		display:inline;
    		margin-right:5px;
    		margin-top:5px;
    	}

    	#title{
    		font-size:200%;
    		margin-left:2%;
    		margin-top:2px;
    		color:rgba(0,0,0,.70);
    		letter-spacing:3px;
    	}
    	.title{
    		display:block;
    		float:left;
    		background-color:#C5CFD4;
    		padding-left:10px;
    		padding-right:10px;
    		border-radius:5px;
    		color:rgb(255,255,255);
    	}
    	

    	#algorithms_menu button{
    		width:80px; 
    	}

    	#algorithms_menu{
    		width:40%;
    		min-width:400px;
    	}
    </style>
</head>

<body>
  
  <div id="header">
    <div id="title" style="float:left; display:inline;"><b><i>CDL Capital</i></b></div>
    <div id="logout"> Logged in as <b><u>${username}$</b></u> <button class="btn btn-danger" style="margin-left:3px" onclick="logout();">Log Out</button></div>
    
  </div>
  <br><br><br>
  
  <div class="container">
    <div><img style="margin-left:10%;" src="http://cliparts.co/cliparts/rcn/Kxo/rcnKxonLi.png"/></div>
    
    <ul class ="nav nav-tabs">
      <li class="active"><a data-toggle="tab" href="#home">Portfolio</a></li>
      <li><a data-toggle="tab" href="#menu1">Transactions</a></li>
      <li><a data-toggle="tab" href="#menu2" onclick="most_active_stocks(); most_active_stocks_volume();" >Trending</a></li>
      <li><a data-toggle="tab" href="#algorithms_menu" onclick="fetchAlgo(); displayActive(); ">Algorithms</a></li>
      <li><a data-toggle="tab" href="#settings_menu">Settings</a></li>
      
    </ul>
    <br>
    
    
    <div class="tab-content" >
      
      <div id="algorithms_menu"  class="tab-pane fade">
	    <div id="algo_menu" class="panel panel-success">
	    </div>
	    
        <hr>
	    <div id="active_algos" class="panel panel-danger">
	    </div>
        
        <div class="dropdown" id="algorithm_graph_dropdown_types_div" > 
          <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" style="width:150px;">Graph Type<span class="caret"></span></button>
          <ul id="algorithm_graph_dropdown_types" class="dropdown-menu"> 
            
                                    
            <li><a href="#" onClick="draw_algorithm_line_graph('Total Volume Traded')">Total Volume Traded</a></li>

          </ul>
        </div>

        <div class="dropdown" id="algorithm_graph_dropdown_lines_div"> 
          <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown" style="width:150px;">Filter<span class="caret"></span></button>
          <ul id="algorithm_graph_dropdown_lines" class="dropdown-menu"> </ul>
        </div>

    

        <!--<select id="algorithm_graph_dropdown" class="form-control"  name="algorithm_graph_dropdown"></select>-->
        <div id="graph_container" style="width: 1200px; height: 600px; margin0 auto"></div>	

      </div>
      
      
      
      <div id="settings_menu" class="tab-pane fade">
	<div style="width:50%; float:left; display:inline;">
	  <div class="panel panel-info" style="width:90%; ">
	    <div class="panel-heading">Create New User</div>
	    <div id="settings_create_user" class="panel-body">
	      Username : <input id="create_user_username" class="form-control" type="text"/>
	      First Name: <input id="create_user_first_name" class="form-control" type="text"/>
	      Last Name: <input id="create_user_last_name" class="form-control" type="text"/>
	      Password : <input id="create_user_passcode" class="form-control" type="password"/>
	      Verify Password: <input id="create_user_verify" class="form-control" type="password"/>
	      <br><button class="btn btn-info" onclick="create_user();">Create User</button>
	    </div>
	    
	  </div>
	  
	  
	  <div class="panel panel-info" style="width:90%; ">
	    <div class="panel-heading">Update Information</div>
	    
	    <div id="settings_update_body" class="panel-body" id="update_info">
	      First Name: <input id="update_info_first_name" class="form-control" type="text"/>
	      Last  Name: <input id="update_info_last_name"class="form-control" type="text"/>
	      
	      <br><button class="btn btn-info" onclick="update_info();">Update</button>
	    </div>			      
	  </div>
	  
	</div>
	
	<div style="width:50%; float:left; display:inline;">
	  
	  
	  <div class="panel panel-danger" style="width:90%; margin-left:10%;">
	    <div class="panel-heading">Update Password</div>
	    <div id="settings_update_password" class="panel-body">
	      Old Password: <input id="update_password_old" class="form-control" type="password"/>
	      New Password  <input id="update_password_new" class="form-control" type="password"/>
	      Verify Password <input id="update_password_verify" class="form-control" type="password"/>
	      <br><button class="btn btn-danger" onclick="update_password()">Update</button> 
	    </div>
	    
	  </div>
	</div>
	
      </div>
      
      
      <div id="menu1" class="tab-pane fade">
	<br>
	
			


	<div style="width:50%; display:inline; float:left" >
	  <form id="deposit_form" role="form">
	    <div class="panel panel-info" style="width:90%;">
	      <div class="panel-heading">Deposits</div>
	      <div id="deposits" class="panel-body">
		Amount: <input id="amount" class="form-control" type="text"/><br>
		<button class="btn btn-info" onclick="Deposit()">Deposit</button>
	      </div>
	    </div>
	  </form>
	  
	</div>
	<div style="width:50%; display:inline; float:left;">
	  <form id="buy_form" role="form" rol="form">
	    <div class="panel panel-warning" style="width:100%; ">
	      <div class="panel-heading">Buy</div>
	      <div id="deposits" class="panel-body">
		Company: <input id="company_name_buy" type="text" class="form-control" name="company_name" /><br>
		Volume: <input id="volume_buy" class="form-control" type="number" min="0" name="volume_buy" /><br>
		<button class="btn btn-warning" id="Buy" onclick="buy()">Buy</button>
	      </div>
	    </div>
	  </form>
	  
	  
	  
	  <form id="sell_form" role="form" rol="form">
	    <div class="panel panel-warning" style="width:100%;  ">
	      <div class="panel-heading">Sell</div>
	      <div id="sells" class="panel-body">
		Company: <select id="company_name_sell" class="form-control"  name="company_name_sell"></select>
		Volume: <input id="volume_sell" class="form-control" type="number" min="0" name="volume_sell" /><br>
		<button class="btn btn-warning" id="Sell" onclick="sell()">Sell</button>
	      </div>
	    </div>
	  </form>
	</div>
	
	
	
	
	
	
      </div>
      
      <div id="home" class="tab-pane fade in active">
	<div class="dropdown">
	  <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Portfolio Filter<span class="caret"></span></button>
	  <br>
	  <ul id="portfolio_filter_dropdown" class="dropdown-menu">
	  </ul>
	</div>
	
	<div class="row">
	  <div class="col-sm-6" sidenav>
	    <h2><b><u>Portfolio Information</u></b></h2>
	    <table class="table table-hover user_table">
	      <thead>
		<tr>
		  <th>Total Portfolio</th>
		  <th>Available Funds</th>
		  <th>Total Deposited</th>
		  <th>Total Stock Value</th>
		  <th>Total Gain/Loss</th>
		</tr>
	      </thead>
	    </table>
 
	    <h2><b><u>Owned Stocks</u></b></h2>
	    <div style= "overflow:auto; max-height:400px;">
	      <table class="table table-hover owned_stocks_table">
		<thead>
		  <tr>
		    <th>Stock</th>
		    <th>Shares</th>
		    <th>Current Price</th>
		    <th>Total Worth</th>
		    <th>Gain/Loss</th>
		  </tr>
		</thead>
	      </table>
	    </div>

	    <br>
	    
	    <h2><b><u>Transaction History</u></b></h2>
	    <div style="overflow:auto; max-height:400px;">
	      <table class="table table-hover transaction_table" >
		<thead>
		  <tr>
		    <th>Transaction Date </th>
		    <th>Transaction Type</th>
		    <th>Stock</th>
		    <th>Price</th>
		    <th>Total Price</th>
		    <th>Volume</th>
		  </tr>
		</thead>
	      </table>
	    </div>
	  </div>
	  <div class="col-sm-6" sidenav>
	     <div><h2><b><u>Top Invested Companies</u></b></h2></div>
	     <div><div id="owned_stocks_chart" style="width:500px; height:500px;"></div></div>
 

	    <div><h2><b><u>Top Invested Industries</u></b></h2></div>
	    <div id="sector_chart" style="width: 500px; height: 550px; float:right;"></div>
	    
	   
  
	  </div>
	</div>	
      </div>
          
      <div id="menu2" class="tab-pane fade">	
	<div class="row">
	  <div class="col-sm-6">
	    <h2><b><u>Percent Change In Price</u></b></h2>				
	    <div>
	      <br>
	      <h4>Top 25 Positive Changes</h4>
	      <div style= "overflow:auto; height:350px;">
		<table class="table table-hover percentchange_max_table" >
		  <thead>
		    <tr>
		      <th>Stock</th>
		      <th>Percent Change</th>
		    </tr>
		  </thead>
		</table>
	      </div>
	    </div>
	    
	    <div>
	      <br>
	      <h4>Top 25 Negative Changes</h4>
	      <div style="overflow:auto; height:350px">
		<table class="table table-hover percentchange_min_table" >
		  <thead>
		    <tr>                                                      
		      <th>Stock</th>
		      <th>Percent Change</th>
		    </tr>
		  </thead>
		</table>
	      </div>
	    </div>
	  </div>
	  
	  <div class="col-sm-6">
	    <h2><b><u>Percent Change in Daily Volume</u></b></h2>
	    <br>
	    <h4>Top 25 Percent Change</h4>
	    <div style="overflow:auto; height:800px">
	      <table class="table table-hover volumechange_max_table">
		<thead><tr>
		    <th>Stock</th>
		    <th>Percent Change</th>
		</tr></thead>
	      </table>
	    </div>
	    
	  </div>
	</div>
	
	
	<br>
	<br>
	<div id="transaction_information"></div>
      </div>
    </div>
    <br/>
    <br/>
  </div>
  


<script type="text/javascript">
  
    function algorithm_graph_result(){ 
        var algorithm_graph_result = $.ajax({
          		type: 'POST',
          		url: '${algorithm_graph_link}$',
          		data: 'username='+ '${username}$',
          		dataType: "json",
          		async: false}).responseText;

          	var json_obj=JSON.parse(algorithm_graph_result);
            console.log(json_obj)
            return json_obj
    }    
    
      
 
    // Doesn't do anything, never did anything, might use later
    /*
    function json_to_graph_data(json_obj)
    {   
        
        for (var i=(parseInt(upload_company_data[0]['query']['count'])-1); i>=0; i--)
        {
            //stock_data.push([upload_company_data[0]['query']['results']['quote'][i]['Date'], parseFloat(upload_company_data[0]['query']['results']['quote'][i]['Adj_Close'])]);
            var i_date = new Date(upload_company_data[0]['query']['results']['quote'][i]['Date']);
            console.log("LOOP: " + i_date);
            stock_data.push([Date.UTC(i_date.getFullYear(), i_date.getMonth(), i_date.getDate()), parseFloat(upload_company_data[0]['query']['results']['quote'][i]['Adj_Close'])]);
        }
    }
    */
   
    function draw_algorithm_line_graph(type)
    {
        //algorithm_graph_result()
        data = algorithm_graph_result();
        //console.log(field);
        var graph_1 = [];
        graph_1.push({name: "Total", data: data});
        
   
        $(function () {
            $('#graph_container').highcharts({
                title: {
                    text: type,
                    x: -20 //center
                },
                subtitle: {
                    text: '',
                    x: -20
                },
                xAxis: {
                    tickInterval: 1,
                //    type: 'datetime',
                //    dateTimeLabelFormats: {
                //        month: '%b %Y',
                //        year: '%Y'
                //    },
                    title: {
                        text: 'Days'
                    }
                },
                yAxis: {
                    title: {
                        text: 'Number of Trades'
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#808080'
                    }]
                },
                tooltip: {
                    valueSuffix: ' shares'
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle',
                    borderWidth: 0
                },
                //series: [{
                //    name: 'Algo',
                //    data: data
                //}]
                series: graph_1
            });
        });        

    }



    function algorithm_graph_dropdown()
    {
        var user_name="${username}$";
        var generate_algorithm_graph_dropdown="generate_algorithm_graph_dropdown";
        var generate_algorithm_graph_dropdown_parsed = [];

        var generate_algorithm_graph_dropdown_result = $.ajax({
            type: 'POST',
           	url: "${algorithm_graph_dropdown_link}$",
           	data: 'user_name='+ user_name,
           	dataType: "json",
           	async: false}).responseText;
        console.log(generate_algorithm_graph_dropdown_result);
        generate_algorithm_graph_dropdown_parsed=JSON.parse(generate_algorithm_graph_dropdown_result);
        console.log(generate_algorithm_graph_dropdown_parsed);
        $('#algorithm_graph_dropdown').empty();
        //$('<option value="Companies"> Algorithms </option>').appendTo('#algorithm_graph_dropdown');
        for(var field in generate_algorithm_graph_dropdown_parsed) 
        {
            $('<li><input type ="checkbox" name="algorithm_graph_checkbox" value=" ' + field + ' ">' + field + '<br></li>').appendTo('#algorithm_graph_dropdown_lines');
            //$('<li><a href="#" onClick="draw_algorithm_line_graph('+generate_algorithm_graph_dropdown_parsed[field]+');">' + field + '</a></li>').appendTo('#algorithm_graph_dropdown');
        }
    }  
   
    draw_algorithm_line_graph('Total Volume Traded');
    algorithm_graph_dropdown();

</script>





  <script type="text/javascript">
    
      var intervalId = null;
      window.onload = start;
      
      function set_filter_cookie(filter)
      {
        document.cookie = "filter="+filter;
      }

      function getCookie(cname)
      {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++)
	{
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1);
		if (c.indexOf(name) == 0) return c.substring(name.length,c.length);
	}
	return "";
      }
      
      function start()
      {
        set_filter_cookie(1);
      	generate_sell_drop_down();
	generate_filter_dropdown();
      	get_company_names();
      	update_profile_information();
      	intervalId = setInterval(update_profile_information, 600000);
      }

      function update_profile_information()
      {
        filter = getCookie("filter");
        var update_profile_result = $.ajax({
      		type: 'POST',
      		url: '${upload_link}$',
      		data: 'username='+ '${username}$'  + '&filter='+ filter,
      		dataType: "json",
      		async: false}).responseText;

      	var json_obj=JSON.parse(update_profile_result);
        //		console.log(json_obj);
        table_generate_users(json_obj['users']);
        table_generate_transactions(json_obj['transactions']);
        table_generate_owned_stocks(json_obj['owned_stocks']);
        displayChart(json_obj['chart_axis'],json_obj['chart_data'],'#sector_chart',' stocks' , 'volume')
				  //drawChart();

	displayChart(json_obj['owned_stocks_chart_axis'],json_obj['owned_stocks_chart_value'],'#owned_stocks_chart',' USD','price')
			
                //load_profile_information();
                //most_active_stocks();
                //most_active_stocks_volume();
				  }

				  function displayChart(chart_axis, chart_data,chart_div,suffix, tooltip){
				 
				  if(chart_axis.length<10){
							 document.getElementById('sector_chart').style.height='500px';
							 }
				  
				  $(function () {
				  $(chart_div).highcharts({
				  chart: {
				  plotBackgroundColor: null,
				  plotBorderWidth: null,
				  plotShadow: false,
				  type: 'bar'
				  },

				  xAxis: {
				  categories: chart_axis,
				  title: {
				  text: null
				  }
				  },

				  title: {
				  text: ' '
				  },

				  plotOptions: {
				  bar:{
				  dataLabels:{enabled:true}
				  }
				  },
				  tooltip:{
				  valueSuffix: suffix,
				  },
				  series: [{
				  name: tooltip,
				  colorByPoint: true,
				  data: chart_data
				  }]
				  });
				  });
				  }
				  
				  

            function table_generate_owned_stocks (json_obj)
            {
            	$('.owned_stocks_table tr td').remove();
            	var tb = document.createElement("tbody");		
            	
                var count = 0;
            	for (i in json_obj)
                {
            		var tr = document.createElement("tr");
            		var td1 = document.createElement("td");
            		var td2 = document.createElement("td");
            		var td3 = document.createElement("td");
            		var td4 = document.createElement("td");
            		var td5 = document.createElement("td");

            		var t1 = document.createTextNode(json_obj[i]['stock']);
            		td1.appendChild(t1);
            		var t2 = document.createTextNode(json_obj[i]['current_shares']);
            		td2.appendChild(t2);
            		var t3 = document.createTextNode(json_obj[i]['current_price']);
            		td3.appendChild(t3);
            		var t4 = document.createTextNode(json_obj[i]['total_worth']);
            		td4.appendChild(t4);
            		var t5 = document.createTextNode(json_obj[i]['profit']);
            		td5.appendChild(t5);

            		tr.appendChild(td1);
            		tr.appendChild(td2);
            		tr.appendChild(td3);
            		tr.appendChild(td4);
            		tr.appendChild(td5);

            		tb.appendChild(tr);
            	}
            	
            	var $formrow = tb
            	$('.owned_stocks_table').append($formrow);
            	
            }

            function table_generate_transactions (json_obj)
            {
            	$('.transaction_table tr td').remove();
            	var tb = document.createElement("tbody");
            	
            	len = Object.keys(json_obj).length;

            	for (i=len-1; i>=0; i--)
            	{

            		var tr = document.createElement("tr");
            		var td1 = document.createElement("td");
            		var td2 = document.createElement("td");
            		var td3 = document.createElement("td");
            		var td4 = document.createElement("td");
            		var td5 = document.createElement("td");
            		var td6 = document.createElement("td");
            		
            		var t1 = document.createTextNode(json_obj[i]['trans_date']);
            		td1.appendChild(t1);
            		var t2 = document.createTextNode(json_obj[i]['trans_type']);
            		td2.appendChild(t2);
            		var t3 = document.createTextNode(json_obj[i]['stock']);
            		td3.appendChild(t3);
            		var t4 = document.createTextNode(json_obj[i]['price']);
            		td4.appendChild(t4);
            		var t5 = document.createTextNode(json_obj[i]['total_price']);
            		td5.appendChild(t5);
            		var t6 = document.createTextNode(json_obj[i]['volume']);
            		td6.appendChild(t6);
            		
            		tr.appendChild(td1);
            		tr.appendChild(td2);
            		tr.appendChild(td3);
            		tr.appendChild(td4);
            		tr.appendChild(td5);
            		tr.appendChild(td6);
            		
            		tb.appendChild(tr);
            	}

            	var $formrow = tb;
            	$('.transaction_table').append($formrow);
            	
            }



            function table_generate_users (json_obj)
            {
            	var tb = document.createElement("tbody");
            	var tr = document.createElement("tr");

            	var td1 = document.createElement("td");
            	var td2 = document.createElement("td");
            	var td3 = document.createElement("td");
            	var td4 = document.createElement("td");
            	var td5 = document.createElement("td");

            	var t1 = document.createTextNode(json_obj['total_portfolio']);
            	td1.appendChild(t1);
            	var t2 = document.createTextNode(json_obj['available_funds']);
            	td2.appendChild(t2);
            	var t4 = document.createTextNode(json_obj['total_stock_values']);
            	td4.appendChild(t4);
            	var t5 = document.createTextNode(json_obj['profit']);
            	td5.appendChild(t5);
            	var t3 = document.createTextNode(json_obj['total_deposited']);
            	td3.appendChild(t3);

            	tr.appendChild(td1);
            	tr.appendChild(td2);
            	tr.appendChild(td3);
            	tr.appendChild(td4);
            	tr.appendChild(td5);

            	tb.appendChild(tr);

            	var $formrow = tb;

            	$('.user_table tr td').remove();
            	$('.user_table').append($formrow);
            }


            
            function Deposit()
            {
            	var amount=document.getElementById('amount');

            	if(amount.value > 0)
            	{
            		var deposit_result = $.ajax({
            			type: 'POST',
            			url: '${deposit_link}$',
            			data: 'username='+ '${username}$' + '&amount='+ amount.value,
            			dataType: "datastring",
            			async: false}).responseText;

            		document.getElementById('deposit_status').innerHTML = deposit_result;
            		update_profile_information();
            	}
            	
            	document.getElementById("deposit_form").reset();
            }

            function buy()
            {
            	var company_name=document.getElementById('company_name_buy');
            	var volume=document.getElementById('volume_buy');

            	if(volume.value > 0)
            	{
            		var buy_result = $.ajax({
            			type: 'POST',
            			url: '${transaction_link}$',
            			data: 'username='+ '${username}$' + '&company='+ company_name.value + '&volume='+ volume.value + '&trans_type=buy' + '&algo_id=0',
            			dataType: "json",
            			async: false}).responseText;
		        //console.log(buy_result)
		        update_profile_information();
		    }
		    generate_sell_drop_down();
		    document.getElementById("buy_form").reset();
		}
		
	    function sell()
	    {
			var company_name=company_name_sell.value;
			var volume=document.getElementById('volume_sell');
			
			if(volume.value > 0)
			{
				var sell_result = $.ajax({
					type: 'POST',
					url: '${transaction_link}$',
					data: 'username='+ '${username}$' + '&company='+ company_name + '&volume='+ volume.value + '&trans_type=sell' + '&algo_id=0',
					dataType: "json",
					async: false}).responseText;

				update_profile_information();
			}
                //console.log(sell_result);
                document.getElementById("sell_form").reset();
                generate_sell_drop_down();
                
            }

            function generate_filter_dropdown()
            {
                 var user_name = "${username}$";

                 var generate_filter_dropdown_result = $.ajax({
            		type: 'POST',
            		url: "${filter_link}$",
            		data: 'user_name='+ user_name,
            		dataType: "json",
                        async: false}).responseText;
      
                    generate_filter_dropdown_parsed=JSON.parse(generate_filter_dropdown_result);
                    console.log(generate_filter_dropdown_parsed);
                    
                    $('#portfolio_filter_dropdown').empty();
                    
                    for(var field in generate_filter_dropdown_parsed) {
                    	$('<li><a href="#" onClick="set_filter_cookie('+generate_filter_dropdown_parsed[field]+');update_profile_information();">' + field + '</a></li>').appendTo('#portfolio_filter_dropdown');
                    }
            }
            
            function generate_sell_drop_down()
            {
            	var user_name="${username}$";
            	var generate_sell_drop_down="generate_sell_drop_down";
            	var generate_sell_drop_down_parsed = [];

            	var generate_sell_drop_down_result = $.ajax({
            		type: 'POST',
            		url: "${dropdown_link}$",
            		data: 'user_name='+ user_name + '&sell_companies_list='+ generate_sell_drop_down,
            		dataType: "json",
            		async: false}).responseText;
                    //console.log(generate_sell_drop_down_result);
                    generate_sell_drop_down_parsed=JSON.parse(generate_sell_drop_down_result);
                    //console.log(generate_sell_drop_down_parsed);
                    $('#company_name_sell').empty();
                    $('<option value="Companies"> Companies </option>').appendTo('#company_name_sell');
                    for(var field in generate_sell_drop_down_parsed) {
                    	$('<option value="'+ generate_sell_drop_down_parsed[field] + '">' + generate_sell_drop_down_parsed[field] + '</option>').appendTo('#company_name_sell');
                    }
                }
                

      /*function load_profile_information()
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
            };*/

            
            function most_active_stocks()
            {
            	var most_active_stocks_result = $.ajax({
            		type: 'POST',
            		url: '${active_stocks_percentchange_link}$',
            		data: 'user_name='+ '${username}$',
            		async: false}).responseText;
            	var most_active_stocks_result_parsed = JSON.parse(most_active_stocks_result);
	//	console.log(most_active_stocks_result_parsed);
	
	table_generate_active_stocks_percentchange (most_active_stocks_result_parsed);
	
}


function table_generate_active_stocks_percentchange (json_obj)
{
	$('.percentchange_min_table tr td').remove();
	var tb = document.createElement("tbody");

	var worst_changes = json_obj[0];	
	var best_changes = json_obj[1];	
		//console.log(worst_changes[0]["symbol"]);					
		// Doing the negative changes
		for (i=0; i < worst_changes.length; i++)
		{
			
			var tr = document.createElement("tr");
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			td2.style.color = "red";

			var t1 = document.createTextNode(i+1 + ". " + worst_changes[i]['symbol']);
			td1.appendChild(t1);
			var t2 = document.createTextNode(Math.round(worst_changes[i]['PercentChange']*100)/100 + " %");
			td2.appendChild(t2);


			tr.appendChild(td1);
			tr.appendChild(td2);
			tb.appendChild(tr);
		}

		

		var $formrow = tb
		$('.percentchange_min_table').append($formrow);

		
		
		
		$('.percentchange_max_table tr td').remove();
		var tb = document.createElement("tbody");

		// Doing the positive changes
		for (i=0; i < best_changes.length; i++)
		{ 
			
			var tr = document.createElement("tr");
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			
			td2.style.color = "green";
			
			var t1 = document.createTextNode(i+1 + ". " + best_changes[i]['symbol']);
			td1.appendChild(t1);
                        var t2 = document.createTextNode("+" + Math.round(best_changes[i]['PercentChange']*100)/100 + " %"); // Add the + sign for display
                        td2.appendChild(t2);

                        tr.appendChild(td1);
                        tr.appendChild(td2);

                        tb.appendChild(tr);
                    }

                    var $formrow = tb
                    $('.percentchange_max_table').append($formrow);
                    
                }

                function most_active_stocks_volume()
                {
                	var most_active_stocks_volume_result = $.ajax({
                		type: 'POST',
                		url: '${active_stocks_volumechange_link}$',
                		data: 'user_name='+ '${username}$',
                		async: false}).responseText;
                	var most_active_stocks_volume_result_parsed = JSON.parse(most_active_stocks_volume_result);
		//console.log(most_active_stocks_volume_result_parsed);

		table_generate_active_stocks_volumechange(most_active_stocks_volume_result_parsed);
	}

	function table_generate_active_stocks_volumechange (json_obj)
	{
		$('.volumechange_max_table tr td').remove();
		var tb = document.createElement("tbody");

		for (i=0; i <json_obj.length; i++)
		{
			
			var tr = document.createElement("tr");
			var td1 = document.createElement("td");
			var td2 = document.createElement("td");
			td2.style.color = "green"
			
			var t1 = document.createTextNode(i+1 + ". " + json_obj[i]['symbol']);
			td1.appendChild(t1);
			var t2 = document.createTextNode(Math.round(json_obj[i]['volume_change']*100)/100 + " %");
			td2.appendChild(t2);

			tr.appendChild(td1);
			tr.appendChild(td2);
			tb.appendChild(tr);			
		}

		var $formrow = tb
		$('.volumechange_max_table').append($formrow);

	} 
	function get_company_names()
	{
		var stock_symbol_list_result = $.ajax({
			type: 'POST',
			url: '${stock_symbol_link}$',
			async: false}).responseText;
              //console.log(stock_symbol_list_result)
              var stock_symbol_list_parsed = JSON.parse(stock_symbol_list_result);
	      //console.log(stock_symbol_list_parsed)
	      $(function() {
	      	$( "#company_name_buy" ).autocomplete({
	      		source: function(request, response) {
	      			var results = $.ui.autocomplete.filter(stock_symbol_list_parsed, request.term);
	      			response(results.slice(0, 10));
	      		}
	      	});
	      });

	  }

	  function fetchAlgo(){
	  	$.ajax({
	  		type: "POST",
	  		url: "${display_algorithms_link}$",
	  		data: {"user_name":"${username}$"},
	  		async: false,
	  		success: function(result){
	  			html="<div class='panel-heading'>Available Algorithms</div><div class='panel-body'><select id='algos' class='form-control'><option value=''>Select Algorithm</option>"  
	  			result=JSON.parse(result)
	  			for (i in result){
	  				html+="<option value='"+result[i]["algo_id"] +"'>" + result[i]["algo_name"] + "</option>";
	  			}
	  			html+="</select> <button class='btn btn-success' onclick='executeAlgo(); resetAlgo();'>Execute</button></div>";
	  			$("#algo_menu").html(html);
	  		}
	  	})
	  	

	  }


	  function executeAlgo(){
	  	var e = document.getElementById("algos");
	  	var algo_id = e.options[e.selectedIndex].value;
	  	
	  	$.ajax({
	  		type: "POST",
	  		url: "${execute_algo_link}$",
	  		data: {"status":"1", "algo_id":algo_id, user:"${username}$"},
	  		async: false,
	  		success: function(result){
	  			console.log(result)
	  		}
	  	})
	  	
	  	resetAlgo()
	  	
	  }


	  function resetAlgo(){
	  	fetchAlgo()
	  	displayActive()
	  }				      
	  
	  function displayActive(){
	  	$.ajax({
	  		type: "POST",
	  		url: "${get_active_algorithms_link}$",
	  		data: {"user_name":"${username}$"},
	  		async: false,
	  		success:function(result){
	  			result=JSON.parse(result)
	  			html="<div class='panel-heading'>Active Algorithms</div><div class='panel-body'><select id='selected_algos' class='form-control'><option value=''>Select Algorithm</option>"
	  			for (i in result){
	  				html+="<option value='"+result[i]["algo_id"] +"'>" + result[i]["algo_name"]+"</option>"
	  			}

	  			html+="</select> <button class='btn btn-danger' onclick='stopAlgo();'>Stop</button></div>"
	  			$("#active_algos").html(html)
	  		}
	  	});
	  }

	  
	  function stopAlgo(){
	  	var e = document.getElementById("selected_algos");
	  	var algo_id = e.options[e.selectedIndex].value;
	  	
	  	$.ajax({
	  		type: "POST",
	  		url: "${execute_algo_link}$",
	  		data: {"status":"2", "algo_id":algo_id, user:"${username}$"},
	  		async: false,
	  		success: function(result){
	  			console.log(result)
	  		}
	  	})

	  	resetAlgo()
	  	
	  }
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

			var user_name="${username}$";
			var portfolio_distribution ="portfolio_distribution";

			var portfolio_distribution = $.ajax({
				type: 'POST',
				url: "${portfolio_link}$",
				data: 'user_name='+ user_name + '&portfolio_distribution='+ portfolio_distribution,
				dataType: "json",
				async: false}).responseText;
          //  console.log(portfolio_distribution)
        //if (typeof portfolio_distribution !== "") {
        	portfolio_distribution_parsed=JSON.parse(portfolio_distribution);
            //console.log(portfolio_distribution_parsed)
            $(function () {
            	$('#piechart').highcharts({
            		chart: {
            			plotBackgroundColor: null,
            			plotBorderWidth: null,
            			plotShadow: false,
            			type: 'pie'
            		},
            		title: {
            			text: ' '
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
   // }
   
}
function logout(){
	document.cookie="login=False";
	window.location="${login_link}$"
}

function update_info(){
	var passcode=prompt("Please enter your pasword");
	var first_name=document.getElementById("update_info_first_name").value;
	var last_name=document.getElementById("update_info_last_name").value;
	$.ajax({
		type: "POST",
		url: "${update_user_link}$",
		data: {"username":"${username}$","passcode":passcode,"first_name":first_name, "last_name":last_name},
		success: function(result){
			result=JSON.parse(result);
			if(result.status=="Fail"){
				result="<div class='alert alert-danger'>Update Failed</div>";
			}else{
				result="<div class='alert alert-success'>Successfully Updated!</div> ";
			}
			
			result += "<button class='btn btn-info' onclick='refresh_page()'>Reload</button>";
			
			$("#settings_update_body").html(result);
		}});
}

function update_password(){
	var old_passcode=document.getElementById("update_password_old").value;
	var new_passcode=document.getElementById("update_password_new").value;
	var verify=document.getElementById("update_password_verify").value;

	if(verify!==new_passcode){
		alert("Password Mismatch");
		return;
	}

	$.ajax({
		type: "POST",
		url: "${update_password_link}$",
		data:{"username": "${username}$", "old_passcode":old_passcode, "new_passcode":new_passcode, "verify":verify},
		success: function(result){
			result=JSON.parse(result);
			if(result.status=="Fail"){
				result="<div class='alert alert-danger'>Update Failed</div>";
			}else{
				result="<div class='alert alert-success'>Update Successful!</div> ";
			}

			result += "<button class='btn btn-info' onclick='refresh_page()'>Reload</button>";

			$("#settings_update_password").html(result); 
			
		}
	});
	
}

function create_user(){
	var username=document.getElementById("create_user_username").value;
	var first_name= document.getElementById("create_user_first_name").value;
	var last_name= document.getElementById("create_user_last_name").value;
	var passcode= document.getElementById("create_user_passcode").value;
	var verify= document.getElementById("create_user_verify").value;

	if(username == "" || first_name=="" || last_name=="" || passcode=="" || verify==""){
		alert("Incomplete Form");
		return;
	}

	if(passcode!==verify){
		alert("Password Mismatch");
		return;
	}

	$.ajax({
		type: "POST",
		url: "${create_user_link}$",
		data: {"username":username,"passcode":passcode,"first_name":first_name, "last_name":last_name},
		success: function(result){
			
			result=JSON.parse(result);
			if(result.status=="Fail"){
				result="<div class='alert alert-danger'>Create Failed</div>";
			}else{
				result="<div class='alert alert-success'>Successfully Created!</div> ";
			}

			result += "<button class='btn btn-info' onclick='refresh_page()'>Reload</button>";
			
			$("#settings_create_user").html(result);
		}});
}

function refresh_page(){
	location.reload();
}


</script>

</body>

</html>


