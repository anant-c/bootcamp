#!/bin/bash

# 1. Function greet that prints "Hello, [name]"
greet() {
  echo "Hello, $1"
}
greet "Alice"

# 2. Function add that sums two numbers

add() {
  local sum=$(( $1 + $2 ))
  echo "$sum"
}
add 5 7

# 3. Function is_even to check if number is even

is_even() {
  if (( $1 % 2 == 0 )); then
    echo "$1 is even"
  else
    echo "$1 is odd"
  fi
}
is_even 4

# 4. Recursive function countdown from number to zero

countdown() {
  if (( $1 < 0 )); then
    return
  fi
  echo "$1"
  countdown $(( $1 - 1 ))
}
countdown 5

# 5. Function find_max that prints max value in array

find_max() {
  local arr=("$@")
  local max=${arr[0]}
  for num in "${arr[@]}"; do
    if (( num > max )); then
      max=$num
    fi
  done
  echo "Max value: $max"
}
find_max 3 7 2 9 5

# 6. Function calculate_area for rectangle area
calculate_area() {
  local length=$1
  local width=$2
  local area=$(( length * width ))
  echo "Area: $area"
}
calculate_area 5 8

# 7. Function convert_to_uppercase for multiple strings

convert_to_uppercase() {
  local i=1
  for str in "$@"; do
    echo "String $i: ${str^^}"
    ((i++))
  done
}
convert_to_uppercase "hello" "world"

# 8. Function is_directory to check if argument is a directory
is_directory() {
  if [ -d "$1" ]; then
    echo "$1 is a directory"
  else
    echo "$1 is not a directory"
  fi
}
is_directory "/home"


# 9. Function download_file using curl
download_file() {
  curl -O "$1"
}
download_file "https://raw.githubusercontent.com/anant-c/anant-c/refs/heads/main/README.md"

# 10. Function backup_file that creates .bak backup
backup_file() {
  cp "$1" "$1.bak"
  echo "Backup of $1 created as $1.bak"
}
backup_file "testing.txt"

