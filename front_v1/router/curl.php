<?php
class Curl{
    
	function execute($url, $POSTFIELDS, $flag){

		$ch = curl_init($url);
        curl_setopt( $ch, CURLOPT_POST, 1);
        curl_setopt( $ch, CURLOPT_POSTFIELDS, $POSTFIELDS);
        curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt( $ch, CURLOPT_HEADER, 0);
        curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);
        $result = curl_exec($ch);
        curl_close($ch);

        if($flag===1){
            echo $result;
        }else{
            return $result;
        }
  	}

	function execute_json($url, $POSTFIELDS, $flag){

		$sending = json_encode($POSTFIELDS);

		$ch = curl_init($url);
        curl_setopt( $ch, CURLOPT_POST, 1);
        curl_setopt( $ch, CURLOPT_POSTFIELDS, $sending);
        curl_setopt( $ch, CURLOPT_FOLLOWLOCATION, 1);
        curl_setopt( $ch, CURLOPT_HEADER, 0);
        curl_setopt( $ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        	'Content-Type: application/json',
            'Content-Length: ' . strlen($sending))
        );
        $result = curl_exec($ch);
        curl_close($ch);

        if($flag===1){
            echo $result;
        }else{
            return $result;
        }
	}
}
?>
