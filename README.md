# AltiumHisto

Python code to process the license usage CSV file from the Altium Concord Pro Vault. Does not require mucking about with databases and all that.

## Generating the CSV file

1. Using an admin account, sign into the Altium Concord Pro vault via the web interface.
2. Admin > Licenses > Reports tab > Usage Log tab
3. Specify time interval, ok to use "custom" 
4. Click Apply, save CSV (some browsers barf when saving a big CSV file, may need to break it up)

The lines in the CSV file should look like this:

	Altium Designer;PYPM-HCND;Jamieson Olsen;All Users;21.8.1.53;1/18/2022 2:15 PM;1/18/2022 6:21 PM

## Software Environment

This tool is designed to run from the command line in a Linux/UNIX like environment. I use Cygwin to run this on a Windows machine.

## User Database

The names of the users for each division are contained in the corresponding TXT file. This file is used by grep to filter the main CSV file by division. For grep to work properly this TXT file must be in UNIX format (lines terminated with LF, not CR/LF) and no blank lines at the end the of the file.

## Checking the CSV file

Next check the CSV file for any user names that are NOT in the user database files. First create a master list of all users.

	$ cat *.txt > all.txt

Now edit all.txt to insure that each name is on a separate line, no empty or blank lines, and the file must be in UNIX format (lines terminated by LF, not LF/CR). Now run the following command:

	$ grep -v -F -f all.txt 2022.csv

This will list all the lines in the CSV file that reference users NOT present in the all.txt user database. Add these users to the appropriate database file and repeat until there are no unknown users.

## Run the BASH script

	$ ./runalldiv.sh

It takes a few seconds to run all divisions.

## Example output

For each division an .out file will be produced, each containing a histogram:

	#Lic    Hours
	01      495.5
	02      1051.1
	03      1802.5
	04      2200.9
	05      2160.7
	06      726.6
	07      209.1
	08      30.4
	09      2.8
	10      0.0
	11      0.0
	12      0.0
	13      0.0
	14      0.0
	15      0.0
	16      0.0
	17      0.0
	18      0.0
	19      0.0
	20      0.0
	21      0.0
	22      0.0
	23      0.0

In this example, one license was in use for 495.1 hours. Two licenses were in use for 1051.1 hours, and so on.



