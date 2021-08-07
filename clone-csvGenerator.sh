#!/bin/bash

### change the mode and give privilege
chmod +x clone-csvGenerator.sh

### clone the repository
git clone https://github.com/mercy-stephen/rosalind.git

### move into the main folder
cd rosalind

echo " "
echo "Welcome to Rosalind's csv_generator!!"
echo "..."
echo "Running the scripts"
echo "..."

### Handling c files par1
gcc gcc_Vanshika.c

### creating a temporary folder to upload the files
ls > names.txt

### removing bash and script file from the txt file (to avoid running them)
sed -i '/names.txt/d' names.txt
sed -i '/csvGenerator.sh/d' names.txt
sed -i '/members_rosalind.csv/d' names.txt
sed -i '/README.md/d' names.txt
sed -i '/gcc_Vanshika.c/d' names.txt

### setting headers and creating csv
echo "Name,Email,<Slack_username>,<Twitter_handle>,Biostack,<Humming_Distance>" > members_rosalind.csv

## handling c files part2
echo " "
./a.out > temp
sed '1d' temp > temp2
awk -F':' '{print $2}' temp2 > temp;
awk '{printf("%s,", $0)}' temp > temp2;
echo `cat temp2` >> members_rosalind.csv;
sed -i '/a.out/d' names.txt # remove from names.txt
rm temp temp2 a.out #a.out is from compiler in C
echo "Script completed"

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
done

# remove temporary folders
rm temp temp2 names.txt

# final message
echo "..."
echo " "
echo "The programm finish the task!"
echo "Please check 'members_rosalind.csv' to know more about us"
echo " "
echo " "

