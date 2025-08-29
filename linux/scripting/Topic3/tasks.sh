#!/bin/bash

# 1. If statement - print "Hello" if variable x equals 10
x=10
if [ "$x" -eq 10 ]; then
  echo "Hello"
fi

# 2. For loop - print numbers 1 to 5
for i in {1..5}
do
  echo $i
done

# 3. While loop - read numbers until user enters '0'
num=1
while [ "$num" != "0" ]
do
  read -p "Enter a number (0 to quit): " num
done

# 4. Until loop - count down from 5 to 1
count=5
until [ $count -lt 1 ]
do
  echo $count
  ((count--))
done

# 5. Case statement - print messages based on user input
read -p "Enter a fruit: " fruit
case $fruit in
  apple) echo "You chose apple." ;;
  banana) echo "You chose banana." ;;
  orange) echo "You chose orange." ;;
  *) echo "Unknown fruit." ;;
esac


# 6. Multiple nested if statements.

num=15
if [ $num -gt 10 ]; then
  if [ $num -lt 20 ]; then
    echo "Number is between 11 and 19"
  else
    echo "Number is 20 or more"
  fi
else
  echo "Number is 10 or less"
fi

# 7. For loop over array of names, print each name
names=("Alice" "Bob" "Charlie")
for name in "${names[@]}"
do
  echo $name
done

# 8. For loop that breaks after printing third item
items=("one" "two" "three" "four" "five")
count=0
for item in "${items[@]}"
do
  echo $item
  ((count++))
  if [ $count -eq 3 ]; then
    break
  fi
done

# 10. For loop that skips odd numbers in array (continue)

numbers=(1 2 3 4 5)
for num in "${numbers[@]}"
do
  if (( num % 2 != 0 )); then
    continue
  fi
  echo $num
done


# 9. While loop with sleep - print message every 5 seconds
while true
do
  echo "Hello every 5 seconds"
  sleep 5
done



