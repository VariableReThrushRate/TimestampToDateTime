import os as os

currentdir = os.listdir("./images/")
print(currentdir)
# To be Done
# Get input scheme from previous scale project for source and output direetories
# Make a list by making parsed datetime objects out of each file in the directory (do as same time as dict)
# Make a dictionary that caches the file name associated with the datetime object, datetime as key because I'm insane
# For loop that iterates over the list in order and outputs the files with the kdenlive format.