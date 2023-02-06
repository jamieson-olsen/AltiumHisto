# AltiumHisto

Python code to process the license usage CSV file from the Altium Concord Pro Vault. Does not require mucking about with databases and all that.

## Generating the CSV file

1. Using an admin account, sign into the Altium Concord Pro vault via the web interface.
2. Admin > Licenses > Reports tab > Usage Log tab
3. Specify time interval, ok to use "custom" 
4. Click Apply, save CSV (some browsers barf when saving a big CSV file, may need to break it up)

The lines in the CSV file should look like this:

	Altium Designer;PYPM-HCND;Jamieson Olsen;All Users;21.8.1.53;1/18/2022 2:15 PM;1/18/2022 6:21 PM

## User Database

The names of the users for each division are contained in the corresponding TXT file. This file is used by grep to filter the main CSV file by division. For grep to work properly this TXT file must be in UNIX format (lines terminated with LF, not CR/LF) and no blank lines at the end the of the file.

## Run the BASH script

$ ./runalldiv.sh

it takes a few seconds to run all divisions

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



