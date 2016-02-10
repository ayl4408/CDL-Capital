var counter = 10;
var intervalId = null;

window.onload = start;
var i = 0;

/*
function test()
{   
    
    $BASE_URL = "http://query.yahooapis.com/v1/public/yql";
    $yql_query = "env 'store://datatables.org/alltableswithkeys'; select * from yahoo.finance.quotes where symbol in ('GOOG')";
    $yql_query_url = $BASE_URL . "?q=" . urlencode($yql_query) . "&format=json";
    // Make call with cURL
    $session = curl_init($yql_query_url);
    curl_setopt($session, CURLOPT_RETURNTRANSFER,true);
    $json = curl_exec($session);
    // Convert JSON to PHP object
    $obj =  json_decode($json);
    $Ask=$obj->query->results->quote->Ask;
    //echo($Ask);
    
    //i++;
    
	// ======== Gets data for company from DB =======
	var json_array_data = $.ajax({
		type: 'POST',
		url: "front_router.php",
		data: 'c='+ company + '&t='+ time_frame,
		dataType:"json",
		async: false
	    }).responseText; 
	
	closing_data = JSON.parse(json_array_data);
	
    document.getElementById("info").innerHTML = $Ask;
}

*/

var company = "W/E";

function new_test()
{
    document.getElementById("info").innerHTML = i;
    i++;

    // ======== Gets data for company from DB =======
    var json_array_data = $.ajax({
        type: 'POST',
        url: "front_router.php",
        data: 'test_timestamp='+ company,
        dataType:"json",
        async: false
        }).responseText; 
    
    closing_data = JSON.parse(json_array_data);
    
    document.getElementById("ask").innerHTML = closing_data;
}

function start()
{
	intervalId = setInterval(new_test, 5000);
}