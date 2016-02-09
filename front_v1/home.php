<?php
include('session.php');
?>

<!DOCTYPE html>
<html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!--<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>-->
  <script type="text/javascript" src="jquery/jquery-1.9.1.min.js"></script>
  <script type="text/javascript" src="jquery/jquery.autocomplete.min.js"></script>
  
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script src="https://code.highcharts.com/highcharts.js"></script> 
  <script src="graph/front_end_functions.js"></script>
</head>

<body>
  <div class="container">

    <div class="jumbotron">
      <h1>CDL Capital</h1>
      <h5>Quantitative/Financial Analysis</h5>
</br> 
        <ul class="nav nav-pills">
          <li><a href="http://cdl.ddns.net:4098/CDLCapital/Front/profile.php">My Profile</a></li>
          <li class="active"><a href="http://cdl.ddns.net:4098/CDLCapital/Front/home.php">Analysis</a></li>
          <li><a href="http://cdl.ddns.net:4098/CDLCapital/Front/logout.php">Logout</a></li><br/><br/>
        </ul>
    </div>      

<br/>
    <div class="row">
          <form id="upload_company_information_form" class="form-horizontal" role="form">
            <!--<div class="form-group">
                <div class="col-sm-offset-1 col-sm-1">
                  <h4>Search Company</h4>
                </div>
            </div>-->
            <div class="form-group">
              <label class="control-label col-sm-2" for="comp_name">Search Company</label>
              <div class="col-sm-3">
                <input class="form-control" type="text" id="comp_name"/>
              </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-1">
                  <input class="form-control" type="button" value="Submit" onclick="company_information();">
                </div>
            </div>
          </form>
          <div id="outputbox"><p id="outputcontent"></p></div>
<br/>
<br/> 
          <div id="graph_container" style="width:100%; height:400px;"></div>
    </div>

    <div class="row">
      <div class ="col-sm-6">
        <div id="financial_information"></div>
      </div>
      <div class ="col-sm-6">
        <div id="quantitative_analysis"></div>
      </div>
    </div>

    <!--
    <div class="row">

      <div class="col-sm-4">
        
        <h4>Select Company</h4>
        <form>
          <select id="select_company" name="users" onchange="display_graph_stats(select_company.value, 365)">
            <option value="">Companies</option>
              <?php
                /*require('curl.php');
                $front_url = 'http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php';
                $u='post';
                $myvars= 'u=' . $u;
                $obj= new Curl();
                $result = $obj->execute($front_url, $myvars, 0);
                $company_array = json_decode($result);
            
                for($i=0; $i<count($company_array); $i++) {
                  echo "<option value='" . $company_array[$i] . "'>". $company_array[$i] ."</option>";
                }*/
              ?>
          </select>
        </form>

        <form>
          <select id="Days" onchange="display_graph_stats(select_company.value, Days.value)">
            <option value="">Time Frame</option>
            <option value="365">365 Days</option>
            <option value="180">180 Days</option>
            <option value="90">90 Days</option>
            <option value="30">30 Days</option>
            <option value="14">14 Days</option>
            <option value="7">7 Days</option>
          </select>
        </form>
        
        <input id="update" type="button" value="Update Graph" onclick="update_graphs(companies);" />
        <input id="delete" type="button" value="Delete Graph" onclick="del_graph(select_company.value);" />
      </div>

      <div class="col-sm-4">
        <h4>Call Option Simulator</h4>
        
        <form>
            <label>Strike Price </label><input id="strike_price" type="text" name="strike_price"/><br/>
            <label>Expiration Days </label><input id="num_days" type="text" name="num_days"/><br/>
            <input id="calc" type="button" value="Calculate" onclick="calc_python(select_company.value);"/> 
        </form>
      </div>

      <div class="col-sm-4">
        <h4>Search Companies</h4>        
        <form action="front_router.php" method="post" >
            <label>Company Name </label><input type="text" name="comp_name" /><br/>
            <label>Start Date</label><input type="text" name="start_date" /><br/>
            <label>End Date </label><input type="text" name="end_date" /><br/>
            <label></label><input type="submit" value="Upload" name="upload2"><br/>
        </form>
      </div>

    </div>
    -->
    
    <br/><br/>

    <!-- SECOND ROW -->
    <!--<div class="row">

    <div class="col-sm-8">
        <div id="graph_div" style="width:700px; height:400px;"></div>
    </div>

    <div class="col-sm-4">
    
      <div id="data_div">
        <br/>
        <input type="checkbox" id="linear_regression_checkbox" name="linear_reg" onclick="linear_regression()" >Linear Regression<br>
        <div id="max_div"></div>
        <div id="min_div"></div>
        <div id="avg_div"></div>
        <div id="sd_div"></div>
        <br/>
        <div id="py_test"></div>
        <div id="py_test3"></div>
        <div id="py_test2"></div>
      </div>

      </div>

    </div>-->

  </div>

  <!-- GLOBAL COMPANY VARIABLE -->
  <script type="text/javascript"> var companies= '<?php echo $result; ?>'; </script>
  <script>

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
        $('#comp_name').autocomplete({
          lookup: data,
          onSelect: function (suggestion) {
            var thehtml = '<strong>Stock:</strong> ' + suggestion.data + ' <br> <strong>Symbol:</strong> ' + suggestion.value;
            //$('#outputcontent').html(thehtml);
          }
        })
    })

    // Globals
    var stock_data = [];
    var transaction_data = [];
    var buy_sell_data = [];
    //var comp_name=document.getElementById('comp_name');
    var user_name='<?php echo $user_check; ?>';

    function company_information()
    {
      //var comp_name = document.getElementById('comp_name');
      //console.log(comp_name.value);
      //financial_information();
      Upload_company_information();
      financial_information();
      quantitative_analysis();
    }

    function financial_information()
    {
      //comp_name=document.getElementById('comp_name');
      var financial_information = "financial_information";

      // GET ONE YEAR OF STOCK DATA
      var financial_information_result = $.ajax({
        type: 'POST',
        url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
        data: 'financial_information='+ financial_information.value + '&user_name=' + user_name + '&comp_name='+ comp_name.value,
        dataType: "json",
        async: false}).responseText;

      //var financial_information_data = JSON.parse(financial_information_result);
      //console.log(upload_company_information_result);
      //console.log("in financial_information");
      //console.log(financial_information_result);
      console.log(comp_name.value);
      //document.getElementById("financial_information").innerHTML = financial_information_result; 
    }

    function quantitative_analysis()
    {
      //console.log(comp_name);
      //comp_name=document.getElementById('comp_name');
      var quantitative_analysis = "quantitative_analysis";

      // GET ONE YEAR OF STOCK DATA
      var quantitative_analysis_result = $.ajax({
        type: 'POST',
        url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
        data: 'quantitative_analysis='+ quantitative_analysis.value + '&user_name=' + user_name + '&comp_name='+ comp_name.value,
        dataType: "json",
        async: false}).responseText;

      //var financial_information_data = JSON.parse(quantitative_analysis_result);
      //console.log(upload_company_information_result);
      //console.log(quantitative_analysis_result);
      //document.getElementById("quantitative_analysis").innerHTML = quantitative_analysis_result; 
    }
    
    function Upload_company_information()
    {
      //comp_name=document.getElementById('comp_name');
      var upload_company_information = "upload_company_information";

      // GET ONE YEAR OF STOCK DATA
      var upload_company_information_result = $.ajax({
        type: 'POST',
        url: "http://cdl.ddns.net:4098/CDLCapital/Front/router/front_router.php",
        data: 'upload_company_information='+ upload_company_information.value + '&user_name=' + user_name + '&comp_name='+ comp_name.value,
        dataType: "json",
        async: false}).responseText;

      var upload_company_data = JSON.parse(upload_company_information_result);
      //console.log(upload_company_information_result);
      console.log(upload_company_data);

      //Get_user_stocks(comp_name);

      if(upload_company_data[0]['query']['count'] > 0){
        stock_data = [];
        transaction_data = [];


        // ARRAY TO TURN THE JSON INTO JS 2D Array
        for (var i=(parseInt(upload_company_data[0]['query']['count'])-1); i>=0; i--)
        {
          //stock_data.push([upload_company_data[0]['query']['results']['quote'][i]['Date'], parseFloat(upload_company_data[0]['query']['results']['quote'][i]['Adj_Close'])]);
          var i_date = new Date(upload_company_data[0]['query']['results']['quote'][i]['Date']);
          console.log("LOOP: " + i_date);
          stock_data.push([Date.UTC(i_date.getFullYear(), i_date.getMonth(), i_date.getDate()), parseFloat(upload_company_data[0]['query']['results']['quote'][i]['Adj_Close'])]);
        }

        //console.log(upload_company_data[1].length);
        for(var i=(upload_company_data[1].length-1); i>=0; i--)
        {
          var i_date = new Date(upload_company_data[1][i]['trans_date']);
          transaction_data.push([Date.UTC(i_date.getFullYear(), i_date.getMonth(), i_date.getDate()), parseFloat(upload_company_data[1][i]['price'])]);
          buy_sell_data.push([Date.UTC(i_date.getFullYear(), i_date.getMonth(), i_date.getDate()), upload_company_data[1][i]['trans_type']]);
        }

        console.log(upload_company_data[0]['query']['results']['quote'][2]['Date']);
        
        var date = new Date(upload_company_data[0]['query']['results']['quote'][2]['Date']);
        var date2 = new Date("2015-12-10 22:34:26");
        console.log(date);
        console.log(date2);
        console.log(date.getFullYear() + ", " + date.getMonth() + ", " + date.getDay());

        console.log(stock_data);

        //var i_date = new Date(upload_company_data[1][0]['trans_date']);
        //console.log(upload_company_data[1][0]['trans_date']);
        //console.log(Date.UTC(i_date.getYear(), i_date.getMonth()+1, i_date.getDay()));
        //console.log(Date.UTC(1970, 9, 21));
        //console.log(date.getFullYear());
        //console.log(date.getDay());
        //console.log(transaction_data);
        
        // TIME SERIES GRAPH
        $(function () {
          var chart= new Highcharts.Chart({
              chart: {
                  zoomType: 'x',
                  renderTo: 'graph_container'
              },
              title: {
                  text: comp_name.value
              },
              subtitle: {
                  //text: document.ontouchstart === undefined ?
                          //'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
              },
              xAxis: 
              {
                  //type: 'Days'
                  //type: 'datetime',
                  //dateTimeLabelFormats: {
                  //  day: '%y/%m/%d'
                  //},

                  type: 'datetime',
                  dateTimeLabelFormats: { // don't display the dummy year
                      month: '%b %Y',
                      year: '%Y'
                  },
                  title: {
                      text: 'Days'
                  }
              },
              yAxis: 
              {
                  title: {
                      text: 'Price'
                  }
              },
              legend: 
              {
                  enabled: false
              },
              plotOptions: 
              {
                  area: {
                      fillColor: {
                          linearGradient: {
                              x1: 0,
                              y1: 0,
                              x2: 0,
                              y2: 1
                          },
                          stops: [
                              [0, Highcharts.getOptions().colors[0]],
                              [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                          ]
                      },
                      marker: {
                          radius: 2
                      },
                      lineWidth: 1,
                      states: {
                          hover: {
                              lineWidth: 1
                          }
                      },
                      threshold: null
                  }
              },
              series: [{
                  //pointStart: transaction_data[0][0],
                  type: 'area',
                  name: 'Price',
                  data: stock_data
                      },

                      {
                  //pointStart: transaction_data[0][0],
                  name: 'Transaction ',
                  data: transaction_data
                      }
                      ]
            });
          });
        }
          document.getElementById("upload_company_information_form").reset();
      };

    </script>

</body>

</html>