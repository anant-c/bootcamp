#!/bin/bash


# 1. Take filename as input, print number of lines in a loop until empty filename given
while true; do
  read -p "Enter filename (empty to quit): " filename
  if [ -z "$filename" ]; then
    break
  fi
  if [ -f "$filename" ]; then
    lines=$(wc -l < "$filename")
    echo "Number of lines in $filename: $lines"
  else
    echo "File does not exist."
  fi
done

# 2. Redirect output of ls to file directory_list.txt

ls > directory_list.txt


# 3. Read numbers until 'quit' entered, then print sum

while true; do
  read -p "Enter a number (or 'quit' to stop): " input
  if [ "$input" == "quit" ]; then
    break
  fi
  if [[ $input =~ ^[0-9]+$ ]]; then
    ((sum+=input))
  else
    echo "Invalid input, please enter a number or 'quit'."
  fi
done
echo "Sum: $sum"

# 4. Use here document to write multiple lines to a file

cat << EOF > example.txt
This is line 1.
This is line 2.
This is line 3.
EOF

# 5. Take a command as input, execute it, display output
read -p "Enter a command to run: " cmd
eval "$cmd"

# 6. Pipe ls -l output into awk to print only filenames
ls -l | awk '{print $9}'


# 7. Use read to input a string, use grep to check if it’s in a file
read -p "Enter a string to search: " search
read -p "Enter filename: " file
if grep -q "$search" "$file"; then
  echo "String found in $file"
else
  echo "String not found in $file"
fi

# 8. Read CSV file, print each line with fields reversed
while IFS=, read -r f1 f2 f3; do
  echo "$f3,$f2,$f1"
done < file.csv

# 9. Take multiple filenames as arguments, concatenate into new file
cat "$@" > combined.txt

