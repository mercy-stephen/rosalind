﻿#!/usr/bin/perl
 
$Name= 'Vanshika Agarwal ';
$Email= 'vanshika.agarwal98@gmail.com';
$Slack_id = '@Vanshika_16';
$Biostack = 'Data Science, Vaccine informatics, Genomic ';
$twitter= '@Vanshika165';
 
print  ("Name:$Name\n") ;
print ("Email :$email\n") ;
print  ("Slack_id:$Slack_id\n") ;
print ("Biostack:$Biostack\n") ;
print ("Twitter:$twitter\n"); 
$x="Vanshika_16";
$y= "Vanshika165";
$ham_dist=0;
for (my $i=0; $i<length $y; $i++)
     {
      ++$ham_dist if substr($y, $i, 1) ne substr($x, $i, 1);
     }
print(" Hamming Distance :$ham_dist" ) 
