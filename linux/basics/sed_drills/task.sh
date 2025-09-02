#!/usr/bin/env bash

set -e
 
step() {
  echo "[STEP $1] $2"
}
 
safe_exit() {
    echo "[ERROR]: $1"
    exit 1
}

step 1 "Replace the first occurrence of the word 'apple' with 'orange' in a file using sed."
sed -i 's/apple/orange/' sample.txt
sleep 2

step 2 "Delete all lines that contain the word 'error' from a file using sed."
sed -i 's/error//g' sample.txt
sleep 2

step 3 "Append the text 'Hello, world!' to the end of each line in a file using sed."
sed -i 's/$/Hello, world!/' sample.txt
sleep 2

step 4 "Search for lines that start with 'Title: ' and replace it with 'Subject: ' in a file using sed."
sed -i 's/^Title: /Subject: /g' sample.txt
sleep 2

step 5 "Delete all consecutive blank lines, leaving only one blank line between paragraphs, using sed."
sed -i '/^$/d' sample.txt && sed -i 's/$/\n/' sample.txt
sleep 2

step 6 "Print only the lines that contain the word 'important' from a file using sed."
sed -n '/important/p' sample.txt
sleep 2

step 7 "Replace all occurrences of the word 'cat' with 'dog' in a file, considering case-insensitive matching, using sed."
sed -i 's/cat/dog/gi' sample.txt
sleep 2

step 8 "Delete the last line of a file using sed."
sed -i '$d' sample.txt
sleep 2

step 9 "Find lines that start with a number and add a tab character before the number using sed."
sed -i 's/^\([0-9]\)/\t\1/' sample.txt
sleep 2

step 10 "In a CSV file, remove the double quotes surrounding each field using sed."
sed -i 's/"//g' opsCSV.csv
sleep 2
