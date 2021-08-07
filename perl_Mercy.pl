#!usr/bin/perl
$Name= 'Mercy Stephen';
$email= 'mercystephen95@gmail.com';
$Slack_id = '@Mercyme';
$Biostack = 'Drug Development';
$twitter= '@Mercym1';
 
print  ("Name:$Name\n") ;
print ("Email:$email\n") ;
print  ("<Slack_username>:$Slack_id\n") ;
print ("<Twitter_handle>:$twitter\n"); 
print ("Biostack:$Biostack\n") ;
$x="Mercyme";
$y= "Mercym1";
$ham_dist=0;
for (my $i=0; $i<length $y; $i++)
     {
      ++$ham_dist if substr($y, $i, 1) ne substr($x, $i, 1);
     }
print("<hamming_distance>:$ham_dist" ) 
