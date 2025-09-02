#!/usr/bin/env bash
set -e
 
step() {
  echo "[STEP $1] $2"
}

step 1 "If statement - print 'Hello' if variable x equals 10"

x=10 
if [ "$x" -eq 10 ]; then 
  echo "Hello" 
fi 
sleep 2

step 2 "For loop - print numbers 1 to 5"
for ((i=1;i<=5;i++))
do 
  echo $i 
done 
sleep 2

step 3 "While loop - read numbers until user enters '0'"
num=1 
while (( num != 0 )) 
do 
  read -p "Enter a number (0 to quit): " num 
done 
sleep 2

step 4 "Until loop - count down from 5 to 1"

count=5 
until (( count < 1 )) 
do 
  echo $count 
  ((count--)) 
done 
sleep 2

step 5 Case statement - print messages based on user input
read -p "Enter a fruit: " fruit 
case "$fruit" in 
  apple) echo "You chose apple." ;; 
  banana) echo "You chose banana." ;;  
  orange) echo "You chose orange." ;; 
  *) echo "Unknown fruit." ;; 
esac 

sleep 2

step 6 "Multiple nested if statements."

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

sleep 2

step 7 "For loop over array of names, print each name" 
names=("Alice" "Bob" "Charlie") 
for name in "${names[@]}" 
do 
  echo $name 
done 

sleep 2
step 8 "For loop that breaks after printing third item"
items=("one" "two" "three" "four" "five") 
count=0 
for item in "${items[@]}"
do 
  echo $item $((count+1)) 
  ((count=count+1))
  if ((count == 3)); then     
    break 
  fi 
done 

step 10 "For loop that skips odd numbers in array (continue)"

numbers=(1 2 3 4 5) 
for num in "${numbers[@]}" 
do 
  if (( num % 2 != 0 )); then 
    continue 
  fi 
  echo $num 
done 


step 9 "While loop with sleep - print message every 5 seconds"
while true 
do 
  echo "Hello every 5 seconds" 
  sleep 5 
done 



