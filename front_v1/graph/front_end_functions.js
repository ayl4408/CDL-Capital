	var g; //Graph
	var closing_data; // Data
	var coeffs = [ null, null, null ]; // lin reg
	var max, min;
	var counter = 10;
	var intervalId = null;

	console.log("Front End");

  	function display_graph_stats(company, time_frame)
  	{
  		if(company!="")
  		{
	   	    get_data(company, time_frame);
		    display_math(company, time_frame);
		    draw_graph(company, time_frame);
  			//document.getElementById("linReg").style.display = "block";
	  		//document.getElementById("clear_linReg").style.display = "block";
	  		document.getElementById("linear_regression_checkbox").style.display = "block";
	  		document.getElementById("max_div").style.display = "block";
			document.getElementById("min_div").style.display = "block";
			document.getElementById("avg_div").style.display = "block";
			document.getElementById("sd_div").style.display = "block";
		}
		else
		{
			//document.getElementById("linReg").style.display = "none";
			//document.getElementById("clear_linReg").style.display = "none";
			document.getElementById("linear_regression_checkbox").style.display = "block";
			document.getElementById("max_div").style.display = "none";
			document.getElementById("min_div").style.display = "none";
			document.getElementById("avg_div").style.display = "none";
			document.getElementById("sd_div").style.display = "none";
		 	$('#graph_div').empty(); // Graph is cleared
		}
  	}

  	function get_data(company, time_frame)
  	{
  		// ======== Gets data for company from DB =======
	  		var json_array_data = $.ajax({
		      	type: 'POST',
		      	url: "front_router.php",
		      	data: 'c='+ company + '&t='+ time_frame + '&g='+ time_frame,
		      	dataType:"json",
		   		async: false
		   	}).responseText; 
		    	
	   		closing_data = JSON.parse(json_array_data);
		
  	}

	function display_math(company, time_frame)
	{
	    // ======== Gets & Displays Math Data =======

	    var json_array_data = $.ajax({
      		type: 'POST',
      		url: "front_router.php",
      		data: 'c='+ company + '&t='+ time_frame + '&m=' + time_frame,
      		dataType:"json",
      		async: false
	    }).responseText;
	
	    var math = JSON.parse(json_array_data);

	    document.getElementById('avg_div').innerHTML ="Average Closing Price: " + math[0];

	    document.getElementById('sd_div').innerHTML ="Standard Deviation: " + math[1];
	    
	    max = closing_data[0][1], min = closing_data[0][1];
	    for(var i=1; i<closing_data.length; i++)
	    {
	    	if(max < closing_data[i][1]){ max = closing_data[i][1]; }
	    	if(min > closing_data[i][1]){ min = closing_data[i][1]; }
	    }

	    document.getElementById('max_div').innerHTML ="Max Closing Price: " + max;
	    document.getElementById('min_div').innerHTML ="Min Closing Price: " + min;



	}

  	function draw_graph(company, time_frame)
  	{
  		// ======== Draws Graph =======

		g = new Dygraph(
	  		document.getElementById("graph_div"),
	  		closing_data, // Parsed Json 2-D Array being passed
	  		{ // START OF OPTIONS
	    	axes: {
	        	x: {
	            valueFormatter: Dygraph.dateString_,
	            axisLabelFormatter: Dygraph.dateAxisFormatter,
	            ticker: Dygraph.dateTicker
	        	}
	    	},
	    	//valueRange:[min*.95, max*1.05],
	    	underlayCallback: draw_lines,
	    	labels: ['Date','Closing Price'],
	    	yRangePad: (max-min)*.2,
	    	ylabel: 'Closing Prices',
			zoomCallback: linear_regression,
	    	title: company + " " + time_frame + " Day"

	  	}); // END OF OPTIONS         

		clear_lines();

  	}


  	

  	function coefficients(series) 
  	{
  		// ======== Gets Coeffs for drawing Linear Regression =======

	    // Only run the regression over visible points.
	    var range = g.xAxisRange();

	    var sum_xy = 0.0, sum_x = 0.0, sum_y = 0.0, sum_x2 = 0.0, num = 0;
	    for (var i = 0; i < g.numRows(); i++) 
	    {
	        var x = g.getValue(i, 0);
	      	if (x < range[0] || x > range[1]) continue;

	        var y = g.getValue(i, series);
	        if (y === null || y === undefined) continue;
	        if (y.length == 2) 
	        {
	            // using fractions
	        	y = y[0] / y[1];
	        }

	        num++;
	        sum_x += x;
	        sum_y += parseFloat(y);
	        sum_xy += x * y;
	        sum_x2 += x * x;
	    }


	    var a = (sum_xy - sum_x * sum_y / num) / (sum_x2 - sum_x * sum_x / num);
	    var b = (sum_y - a * sum_x) / num;
	    coeffs[series] = [b, a];

	    g.updateOptions({});  // forces a redraw.
	 }

	function draw_lines(ctx, area, layout) 
	{
		// ======== Draws Linear Regression Line =======

		if (document.getElementById("linear_regression_checkbox").checked){
			console.log("checked");
		}
		else
		{
			console.log("unchecked");
			return;
		}


    	if (typeof(g) == 'undefined') 
    	{
    		return;  // won't be set on the initial draw.
		}
        var range = g.xAxisRange();
        for (var i = 0; i < coeffs.length; i++) 
        {
          	if (!coeffs[i]) continue;
         	var a = coeffs[i][1];
         	var b = coeffs[i][0];

        	var x1 = range[0];
          	var y1 = a * x1 + parseFloat(b);
         	var x2 = range[1];
	        var y2 = a * x2 + parseFloat(b);

	        var p1 = g.toDomCoords(x1, y1);
	        var p2 = g.toDomCoords(x2, y2);



		    //var c = Dygraph.toRGB_(g.getColors()[i - 1]);
		    //c.r = Math.floor(255 - 0.5 * (255 - c.r));
		    //c.g = Math.floor(255 - 0.5 * (255 - c.g));
		    //c.b = Math.floor(255 - 0.5 * (255 - c.b));
		    //var color = 'rgb(' + c.r + ',' + c.g + ',' + c.b + ')';
		    var color = "rgb(255, 0 , 0)";
		    ctx.save();
		    ctx.strokeStyle = color;
		    ctx.lineWidth = 1.0;
		    ctx.beginPath();
		    ctx.moveTo(p1[0], p1[1]);
		    ctx.lineTo(p2[0], p2[1]);
		    ctx.closePath();
		    ctx.stroke();
		    ctx.restore(); 

        }
	}


/*

	if (document.getElementById("linear_regression_checkbox") != null) 
	{
    	document.getElementById("linear_regression_checkbox").onchange = linear_regression();
	}
	else 
	{
	   console.log("check box nul");
	}
*/
	//var lin_reg_checkbox = document.getElementById("linear_regression_checkbox");

	//lin_reg_checkbox.onchange = linear_regression();


	function linear_regression()
	{
		coefficients(1);
	}


/*
	function linear_regression()
	{
		if (document.getElementById("linear_regression_checkbox").checked){
			console.log("here");
			coefficients(1); // going to calculate & draw graph
			draw_lines(g.);
		}
		else
		{
			clear_lines();
			console.log("unchecked");
		}
	}
*/

	function clear_lines() 
	{
	    for (var i = 0; i < coeffs.length; i++) coeffs[i] = null;
	    draw_lines();
	}







	function del_graph(company) 
	{
        var x = confirm("Are you sure you want to delete this company?");
        if (x === true) 
        {
            $.ajax({
                type: 'POST',
                url: "https://web.njit.edu/~al356/CDLCapital/index.php",
                data: {dc: company},
                dataType: "dataString",
                async: false});
               $(location).attr('href','https://web.njit.edu/~kad34/CDLCapital/home.php');
        }
	}

     function calc_python(company)
     {

		var strike_price=document.getElementById('strike_price');
		var num_days=document.getElementById('num_days');
		var calculation = $.ajax({
			type: 'POST',
			url: "https://web.njit.edu/~kad34/CDLCapital/front_router.php",
			data: 'sp='+ strike_price.value + '&n='+ num_days.value + '&c='+ company,
			dataType: "json",
			async: false}).responseText;
    		
		var calculation1 = JSON.parse(calculation);
		
    	document.getElementById('py_test').innerHTML = "Current Price: " + calculation1[8];
		document.getElementById('py_test2').innerHTML = "Fair European Call Option Price: " + calculation1[0];
		document.getElementById('py_test3').innerHTML = "Fair Exotic-Asian Option Price: " + calculation1[4];
     } 

     function update_graphs(companies)
     {
     	$.ajax({
     		type: 'POST',
     		url: "https://web.njit.edu/~kc343/CDLCapital/index.php",
     		data: 'updt='+ companies,
     		dataType: "dataString",
     		async: false}).responseText;
     	//console.log(data);

     	$(location).attr('href','https://web.njit.edu/~kad34/CDLCapital/home.php');


     }
     function display(parse_data)
	{
		document.getElementById('daily_company_update').innerHTML = "data: " + parse_data.query.results.quote.symbol + " | created: " + parse_data.query.created + " | Ask: " + parse_data.query.results.quote.Ask ;
	}

	var i=0;
	function start(company)
	{
		var data = $.ajax({
			type: 'POST',
			url: "https://web.njit.edu/~kad34/CDLCapital/front_router.php",
			data: 'company_update='+ company,
			dataType: "json",
			async: false}).responseText;
		console.log(data);
		var parse_data= JSON.parse(data);
		//display(parse_data);
		document.getElementById('daily_company_update').innerHTML = i++;

		//document.getElementById('daily_company_update').innerHTML = "data: " + parse_data.query.created;
		//document.getElementById('daily_company_update').innerHTML = "data: " + parse_data->query->results->quote;
		//$Open = $obj2->query->results->quote[$i]->Open;
	}
	function interval(company)
	{
		intervalId = setInterval(start(company), 5000);
 		 //setTimeout(action, counter * 1000); 
	}

	;