#!/usr/bin/env bash

set -e
 
step() {
  echo -e "\n\n\n[STEP $1] $2"
}
 
safe_exit() {
    echo "[ERROR]: $1"
    exit 1
}

step 1 "Replace the first occurrence of the word 'apple' with 'orange' in a file using sed."
sed  's/apple/orange/' sample.txt || safe_exit "Failed to replace 'apple' with 'orange'"
sleep 2

step 2 "Delete all lines that contain the word 'error' from a file using sed."
sed  's/error//g' sample.txt || safe_exit "Failed to delete lines containing 'error'"
sleep 2

step 3 "Append the text 'Hello, world!' to the end of each line in a file using sed."
sed  's/$/Hello, world!/' sample.txt || safe_exit "Failed to append 'Hello, world!' to each line"
sleep 2

step 4 "Search for lines that start with 'Title: ' and replace it with 'Subject: ' in a file using sed."
sed  's/^Title: /Subject: /g' sample.txt || safe_exit "Failed to replace 'Title: ' with 'Subject: '"
sleep 2

step 5 "Delete all consecutive blank lines, leaving only one blank line between paragraphs, using sed."
sed  '/^$/d' sample.txt && sed  's/$/\n/' sample.txt || safe_exit "Failed to delete consecutive blank lines"
sleep 2

step 6 "Print only the lines that contain the word 'important' from a file using sed."
sed -n '/important/p' sample.txt || safe_exit "Failed to print lines containing 'important'"
sleep 2

step 7 "Replace all occurrences of the word 'cat' with 'dog' in a file, considering case-insensitive matching, using sed."
sed  's/cat/dog/gi' sample.txt || safe_exit "Failed to replace 'cat' with 'dog'"
sleep 2

step 8 "Delete the last line of a file using sed."
sed  '$d' sample.txt || safe_exit "Failed to delete the last line"
sleep 2

step 9 "Find lines that start with a number and add a tab character before the number using sed."
sed  's/^\([0-9]\)/\t\1/' sample.txt || safe_exit "Failed to add tab before numbers"
sleep 2

step 10 "In a CSV file, remove the double quotes surrounding each field using sed."
sed  's/"//g' opsCSV.csv || safe_exit "Failed to remove double quotes from CSV fields"
sleep 2
