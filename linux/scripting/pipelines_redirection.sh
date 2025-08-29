#!/bin/bash

# List all files in /usr/bin that contain the word "python" in their names.
ls -l /usr/bin | grep "python"

# Count the number of files in /usr/bin.
ls -1 /usr/bin | wc -l

# Save the list of files in your home directory to a file named myfiles.txt.
ls -1 /usr/bin > ~/myfiles.txt

# Append the output of date to myfiles.txt.
DATE=$(date)
echo $DATE >> ~/myfiles.txt
# or can do=> date >> ~/myfiles.txt

# check using tail 
tail ~/myfiles.txt

# Sort the contents of myfiles.txt alphabetically and save the result in sorted_myfiles.txt
sort ~/myfiles.txt > ~/sorted_myfiles.txt

