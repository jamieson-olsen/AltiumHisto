# Python code to process the license usage CSV file from the
# Altium Concord Pro Vault. Calculates the number of minutes 1,2,3,...N licenses are in use
# Jamieson Olsen <jamieson@fnal.gov>

import csv
import sys
from datetime import datetime,timedelta

# read in the log file. Only take the files starting with "Altium Designer" and then only
# take the user name string, start time, and end time. In the log the time format is like this
# 2/3/2023 4:02 PM

ActivityList = []
TimeList = []
StripChart = []
Histo = []

if ( len(sys.argv) != 2 ):
    print("usage: adlicense.py input.csv")
    quit()

with open(sys.argv[1], 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    for row in reader:
        if "Designer" in row[0]: # only consider AD and AD-SE license usage, ignore vault usage
            UserName = row[2]
            StartTimeString = row[5]
            ReturnTimeString = row[6]

            StartTime = datetime.strptime(StartTimeString,"%m/%d/%Y %I:%M %p")            
            ReturnTime = datetime.strptime(ReturnTimeString,"%m/%d/%Y %I:%M %p")            

            ActivityList.append([UserName, StartTime, ReturnTime])
            TimeList.append(StartTime)
            TimeList.append(ReturnTime)

# Timelist is a list of timestamps. Every time the number of licenses changes, that timestamp is 
# recorded in Timelist. Sometimes the vault returns a license and immediately checks it out again
# not clear why it does that. So remove dups and sort this list.

TimeList = list(set(TimeList))
TimeList.sort()

# for each timestamp in TimeList, scan through ActivityList and determine how many licenses
# were in use at that moment. Optionally print out this "StripList" showing timestamp and 
# number of licenses in use. Store the StripChart because we'll use this next for making
# a histogram

for t in TimeList:
    LicInUse = 0
    for a in ActivityList:
        if (t >= a[1] and t < a[2]):
            LicInUse = LicInUse + 1
    StripChart.append([t,LicInUse])
    #thermom = "*" * LicInUse
    #print("%s %02d %s" % (t, LicInUse, thermom))

# initialize histogram array for up to 24 licenses in use

for i in range(25):
    Histo.append(timedelta(hours=0))

# scan through StripChart list add up the amount of time each unique number of licenses were in use
# e.g. Histo[4] = time that 4 licenses in use

for i in range(0,len(StripChart)-1):
    Histo[StripChart[i][1]] = Histo[StripChart[i][1]] + (StripChart[i+1][0]-StripChart[i][0])

print("#Lic    Hours");

for i in range(1,25):
    print("%02d\t%.1f" %(i, Histo[i]/timedelta(hours=1)))

