#!usr/bin/bash

## clone repo
git clone .....

## get into the folder
cd rosalind/

## change the mode and give privilege
chmod +x script*

## loop throught all the scripts in the folder
for i in $(ls script*)
do
	./$i | awk -F ',' '{print $1, $2, $3, $4, $5}' >> Team_Sanger.csv
		done
