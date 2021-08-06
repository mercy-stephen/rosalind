#!/bin/bash

### change the mode and give privilege
chmod +x csvGenerator.sh

### clone the repository
#git clone https://github.com/mercy-stephen/rosalind.git

### move into the main folder
#cd rosalind

###
echo " "
echo "Welcome to Rosalin's csv_generator!!"
echo "..."
echo "Running the scripts"
echo "..."

### creating a temporary folder to upload the files
ls > names.txt

### removing bash and script file from the txt file (to avoid running them)
sed -i '/names.txt/d' names.txt
sed -i '/csvGenerator.sh/d' names.txt
sed -i '/members_rosalind.csv/d' names.txt

### setting headers and creating csv
echo "Name,Email,Slack,Twitter,Biostack,H_distance" > members_rosalind.csv

### creating the loop
Lines=$(cat names.txt)
for Line in $Lines; 
do 
	echo " "
	echo "$Line" > temp;  
	awk -F_ '{print $1,$0}' temp > temp2; 
	. temp2 > temp; 
	awk -F':' '{print $2}' temp > temp2; 
	awk '{printf("%s,", $0)}' temp2 > temp;
	echo `cat temp` >> members_rosalind.csv; 
	echo "Script completed"
	rm temp temp2 
done

# remove temporary folders
rm names.txt

# final message
echo "..."
echo " "
echo "The programm finish the task!"
echo "Please check 'members_rosalind.csv' to know more about us"
echo " "
echo " "


