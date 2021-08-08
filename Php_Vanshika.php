#!/usr/bin/php
<!DOCTYPE html>
<html>
<body>

<?php
print "Name:Vanshika Agarwal\n" ;
print "Email:vanshika.agarwal98@gmail.com\n" ;
print "<Slack_username>:@Vanshika_16\n" ;
print "Biostacks:Drug Development & VaccineInformatics & Genomics\n" ;
print "<Twitter_handle>:@Vanshika165\n" ;
function hammingDist($str1, $str2)
{

    $i = 0; $count = 0;

    while (isset($str1[$i]) != '')

    {

        if ($str1[$i] != $str2[$i])

            $count++;

        $i++;

    }

    return $count;
}
 

   

    $str1 = "Vanshika_16";

    $str2 = "Vanshika165";
 

    // function call
    print "<Hamming_Distance>";
    echo hammingDist ($str1, $str2);
?>

</body>
</html>
