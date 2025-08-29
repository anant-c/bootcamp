#!/bin/bash
# Write script to print "hello world"
echo "Hello, World!"

# 2. Create a script that prints the current date and time using the date command.
date

# 3. Write a script to list all files and directories in the current directory using ls.
ls

# 4. Develop a script that prints the name of the current user using the whoami command.
whoami

# 5. Write a script that accepts a username as an argument and prints "Hello, [username]!".
echo "Hello, $1!"

# 6 Create a script to check if a given file exists in the current directory. Accept the filename as an argument.

if [ -e "$2" ]; then
  echo "File '$2' exists."
else
  echo "File '$2' does not exist."
fi


# 7. Develop a script that calculates and prints the factorial of a number provided as an argument.

n=$3
fact=1
for (( i=1; i<=n; i++ ))
do
  fact=$((fact * i))
done
echo "Factorial of $n is $fact"


# 8.Write a script that reads a number from the user and prints whether it is odd or even.

read -p "Enter a number: " num
if (( num % 2 == 0 )); then
  echo "$num is even"
else
  echo "$num is odd"
fi

# 9.Create a script that takes a directory path as an argument and prints the number of files in that directory.

dir=$4
count=$(ls -1 "$dir" | wc -l)
echo "Number of files in $dir: $count"

# 10.Write a script that renames all .txt files in the current directory to .bak.
for file in *.txt
do
  mv "$file" "${file%.txt}.bak"
done
