  <?php
    require('curl.php');
    $front_url = 'https://web.njit.edu/~kad34/CDLCapital/front_router.php';
    $sell_companies_list='post';
    $myvars= 'sell_companies_list=' . $sell_companies_list . '&user_name=' . $user_check;
    $obj= new Curl();
    $result = $obj->execute($front_url, $myvars, 0);
    $company_array = json_decode($result);

    for($i=0; $i<count($company_array); $i++) {
      echo "<option value='" . $company_array[$i] . "'>". $company_array[$i] ."</option>";
    }
  ?>