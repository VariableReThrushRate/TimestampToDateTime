import os
from datetime import datetime

def getdate(name):
   stripname = name.partition('.')[0]
   return datetime.strptime(stripname, "%m%d%Y_%H%M%S")

def fixslash(tofix):
  curros = os.name
  if (tofix[-1]!= "/" and tofix[-1]!= "/"):
    if (curros == "nt"):
      tofix += "\\"
    elif (curros == "posix"):
      tofix += "/"
    else:
      tofix += "/"
    return tofix


# Get Source Directory
sourcedir = input("Enter the source path: ")
while True:
  try:
      sourcedirdata = os.listdir(sourcedir)
      break
  except:
      tscale = input("That did not parse. Please Try again: ")    
      pass

sourcedir = fixslash(sourcedir)

#Get Output Directory
outputdir = input("Enter the output path: ")
while True:
  try:
      os.listdir(outputdir)
      break
  except:
      tscale = input("That did not parse. Please Try again: ")    
      pass

outputdir = fixslash(outputdir)

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

# The entire program centers on this one line. Sheesh.
fileslist.sort()

#Now we begin file copying.
index = 1
for file in fileslist:
   #get the source file name
   sourcefilename = os.path.abspath(sourcedir) + cachedict[file]
   print(sourcefilename)
   #Ouput wound up being complicated.
   # Get the output dir, get the name from index, add the 0s for kdenlive, then get the file extension I forgot from the cachedict. There has to be a beter way to do this. I did not find it.
   outputfilename = os.path.abspath(outputdir) + str(index).zfill(5) + cachedict[file][cachedict[file].rfind('.'):]
   print(outputfilename)
   index += 1


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