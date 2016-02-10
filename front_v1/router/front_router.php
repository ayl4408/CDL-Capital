<?php
    // FRONT ROUTER
    require('curl.php');

    if($_SERVER["REQUEST_METHOD"] == "POST"){

        $headers = getallheaders();
        $middle_url = 'cdl.ddns.net:4098/CDLCapital/Middle/index.php';

        if($_POST["quantitative_analysis"])
        {
            $quantitative_analysis = "quantitative_analysis";
            $comp_name = $_POST["comp_name"];
            $user_name= $_POST['user_name'];
            $myvars = 'quantitative_analysis=' . $quantitative_analysis . '&comp_name=' . $comp_name . '&user_name=' . $user_name;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
        }
        else if($_POST["financial_information"])
        {
            $financial_information = "financial_information";
            $comp_name = $_POST["comp_name"];
            $user_name= $_POST['user_name'];
            $myvars = 'financial_information=' . $financial_information . '&comp_name=' . $comp_name . '&user_name=' . $user_name;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
        }
        else if($_POST["get_stock_symbol"])
        {
            $get_stock_symbol='get_stock_symbol';
            $myvars = 'get_stock_symbol=' . $get_stock_symbol;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
        }
        else if($_POST["upload_company_information"])
        {
            $upload_company_information = "upload_company_information";
            $comp_name = $_POST["comp_name"];
            $user_name= $_POST['user_name'];
            $myvars = 'upload_company_information=' . $upload_company_information . '&comp_name=' . $comp_name . '&user_name=' . $user_name;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
        }
        else if($_POST["update_profile"])
        {
            $user_name = $_POST["user_name"];
            $update_profile="update_profile";
            $myvars = 'update_profile=' . $update_profile . '&user_name=' . $user_name;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
            
        }else if($_POST["portfolio_distribution"]){

            $user_name = $_POST["user_name"];
            $portfolio_distribution = $_POST["portfolio_distribution"];
            $myvars = 'user_name=' . $user_name . '&portfolio_distribution=' . $portfolio_distribution;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if($_POST["sell_companies_list"]){

            $user_name = $_POST["user_name"];
            $sell_companies_list = $_POST["sell_companies_list"];
            $myvars = 'user_name=' . $user_name . '&sell_companies_list=' . $sell_companies_list;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if($_POST["profile_information"]){

            $user_name = $_POST["user_name"];
            $profile_information = $_POST["profile_information"];
            $myvars = 'user_name=' . $user_name . '&profile_information=' . $profile_information;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if($_POST["deposit"]){
            $user_name = $_POST["user_name"];
            $deposit = $_POST["deposit"];
            $amount=$_POST["amount"];
            $myvars = 'user_name=' . $user_name . '&deposit=' . $deposit . '&amount=' . $amount;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
            
        }else if($_POST["sell"]){

            $user_name = $_POST["user_name"];
            $company_name=$_POST["company_name"];
            $volume=$_POST["volume"];
            $type=$_POST["sell"];
            $myvars = 'user_name=' . $user_name . '&company_name=' . $company_name . "&volume=" . $volume . "&sell=" . $type;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if($_POST["buy"]){ //buy stocks

            $user_name = $_POST["user_name"];
            $company_name=$_POST["company_name"];
            $volume=$_POST["volume"];
            $type=$_POST["buy"];
            $myvars = 'user_name=' . $user_name . '&company_name=' . $company_name . "&volume=" . $volume . "&buy=" . $type;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);


        }else if($_POST["m"]){ // Math

            $c=$_POST["c"];
            $t=$_POST["t"];
            $m=$_POST["m"];
            $myvars = 'c=' . $c . '&t=' . $t . '&m=' . $m;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if($_POST["g"]){ // Graph
     
            $c=$_POST["c"];
            $t=$_POST["t"];
            $g=$_POST["g"];
            $myvars = 'c=' . $c . '&t=' . $t . '&g=' . $g;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);
    
        }else if ($_POST['login']) {
    
            $login = $_POST['login'];
            $name = htmlspecialchars($_POST['name']);
            $password  = htmlspecialchars($_POST['password']);
            $myvars = 'name=' . $name . '&password=' . $password . '&login=' . $login;
            $obj= new Curl();
            $result=$obj->execute($middle_url, $myvars, 0);

            if($result != false){
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/home.php');
            }else{
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/login_view.php');
            }
        
        }else if($_POST['register']){
        
            $register = $_POST['register'];
            $name = htmlspecialchars($_POST['name']);
            $password  = htmlspecialchars($_POST['password']);
            $myvars = 'name=' . $name . '&password=' . $password . '&register=' . $register;
            $obj= new Curl();
            $result=$obj->execute($middle_url, $myvars, 0);

            if($result == true){
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/home.php');
            }else{
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/register.php');
            }
        
        }else if ($_POST['upload']){ // CSV Upload (DECOMMISSIONED LEGACY FUNCTION)
        
            $upload = $_POST['upload'];
            $ticker = "";
            $stock = "";
            $stock_symbol_array = array(); 
            $dbhost = "localhost";
            $dbuser = "root";
            $dbpass = "mmGr2016";
            $dbname = "cdlcapital";
            $dbh = mysql_connect($dbhost, $dbuser, $dbpass) or die("Unable to connect to MySQL");
            $selected = mysql_select_db($dbname, $dbh);
            $query = "insert into company_info (symbol, name) values";
            $arrayval = array();
            if(($handle = fopen($_FILES["file"]["tmp_name"], "r")) !== FALSE) 
            {
                while(($line = fgetcsv($handle,9999,",")) !== FALSE)
                {
                    //$buffer= array(); 
                    if($row == 0){
                        $row = 1;
                        continue;
                    }
                    $arrayval[] = "('$line[0]', '$line[1]')";
                    //$buffer['Symbol'] = $line[0];
                    //$buffer['Name'] = $line[1];
                    //$buffer = [$line[0],$line[1]];
                    //array_push($stock_symbol_array, $buffer);       
                }
            }

            fclose($handle);
            
            $query.= implode(',', $arrayval);
            $query_result=mysql_query($query);
            //echo ($query);

            //$obj= new Curl();
            //$result=$obj->execute_json('https://web.njit.edu/~kc343/CDLCapital/index.php', $myvars, 0);
            //var_dump($stock_symbol_array[0]['Symbol']);
        
            /*$upload = $_POST['upload'];
            $date = "";
            $open = "";
            $high = "";
            $low = "";
            $close = "";
            $volume = "";
            $adj_close = "";
            $row = 0;
            $stock_3D_array = array();
            
            if(($handle = fopen($_FILES["file"]["tmp_name"], "r")) !== FALSE) 
            {
                while(($line = fgetcsv($handle,9999,",")) !== FALSE)
                {
                    if($row == 0){
                        $date = $line[0];
                        $open = $line[1];
                        $high = $line[2];
                        $low = $line[3];
                        $close = $line[4];
                        $volume = $line[5];
                        $adj_close = $line[6];
                        $row = 1;
                        $fname = [$_FILES["file"]["name"]];
                        array_push($stock_3D_array, $fname);
                        continue;
                    }
                    array_push($stock_3D_array, $line);       
                }
            }
            fclose($handle);
        
            $obj= new Curl();
            $result=$obj->execute_json($middle_url, $myvars, 0);

            if($result){
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/home.php');
            }else{
                header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/upload.php');
            }*/
        
        }else if ($_POST["sp"]){ // Call Option Form

            $sp=$_POST["sp"];
            $n=$_POST["n"];
            $c=$_POST["c"];
            $myvars = 'sp=' . $sp . '&n=' . $n . '&c='. $c;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if ($_POST['u']){ // Showing Companies

            $u=$_POST['u'];
            $myvars= 'u=' . $u;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

        }else if ($_POST['upload2']){ // DECOMMISSIONED

            $upload2=$_POST['upload2'];
            $start_date=$_POST['start_date'];
            $end_date=$_POST['end_date'];
            $comp_name=$_POST['comp_name'];
            $myvars = 'start_date=' . $start_date . '&end_date=' . $end_date . '&comp_name='. $comp_name . '&upload2='. $upload2;
            $obj= new Curl();
            $obj->execute($middle_url, $myvars, 1);

            header('Location: http://cdl.ddns.net:4098/CDLCapital/Front/home.php');

        }
        else if ($_POST['company_update']){ // DECOMMISSIONED

            $company=$_POST['company_update'];
            $BASE_URL = "http://query.yahooapis.com/v1/public/yql";
            $yql_query = "env 'store://datatables.org/alltableswithkeys'; select * from yahoo.finance.quotes where symbol in ('$company')";
            $yql_query_url = $BASE_URL . "?q=" . urlencode($yql_query) . "&format=json";
            // Make call with cURL
            $session = curl_init($yql_query_url);
            curl_setopt($session, CURLOPT_RETURNTRANSFER,true);
            $json = curl_exec($session);               
            echo $json;
            
        }    
}

?>
