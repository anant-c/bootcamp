#!/usr/bin/env bash

set -e

step(){
  echo -e "[Step $1] $2 \n"
}

safe_exit(){
  echo -e "[ERROR]: $1 \n"
  exit 1
}

step 1 "List all files in /usr/bin that contain the word "python" in their names."
ls -l /usr/bin | grep "python" || safe_exit "Failed to get all files"  
sleep 2

step 2 "Count the number of files in /usr/bin."
ls -1 /usr/bin | wc -l || safe_exit "Failed to count the number of file in usr/bin"
sleep 2
step 3 "Save the list of files in your home directory to a file named myfiles.txt."
ls -1 /usr/bin > ~/myfiles.txt || safe_exit "Failed to save in myfiles.txt"
sleep 2
step 4 "Append the output of date to myfiles.txt."

date >> ~/myfiles.txt || safe_exit "Failed to append date in myfiles.txt"
sleep 2
# check using tail 
tail ~/myfiles.txt
sleep 2

step 5 "Sort the contents of myfiles.txt alphabetically and save the result in sorted_myfiles.txt"
sort ~/myfiles.txt > ~/sorted_myfiles.txt || safe_exit "Failed to sort and store."

