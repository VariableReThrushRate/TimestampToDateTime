import os
from datetime import datetime

def getdate(name):
   stripname = name.partition('.')[0]
   return datetime.strptime(stripname, "%m%d%Y_%H%M%S")

# Get Source Directory
sourcedir = input("Enter the source path: ")
while True:
  try:
      sourcedirdata = os.listdir(sourcedir)
      break
  except:
      tscale = input("That did not parse. Please Try again: ")    
      pass

#Get Output Directory
outputdir = input("Enter the output path: ")
while True:
  try:
      os.listdir(outputdir)
      break
  except:
      tscale = input("That did not parse. Please Try again: ")    
      pass

#Define lists and stuff
cachedict = dict()
fileslist = []

# Begin Processing algo
for name in sourcedirdata:
#Get a conistent date object
    consisdate = getdate(name)
# Add these as date time objects 
    fileslist.append(consisdate)
# The dict associates the file names with the date time they represent, that's why it's a cache
    cachedict[consisdate] = name



#print(fileslist)
#print(cachedict)

#print(outputdir)

# To be Done
# Get input scheme from previous scale project for source and output diretories
# Make a list by making parsed datetime objects out of each file in the directory (do as same time as dict)
# Make a dictionary that caches the file name associated with the datetime object, datetime as key because I'm insane
# For loop that iterates over the list in order and outputs the files with the kdenlive format.
# Kdenlive format is: 00001.jpg
# Make sure to preserve file type when writing files.
# date format: "%m%d%Y_%H%M%S"