#!/usr/bin/env bash

step() {
  echo "[STEP $1] $2"
}
 
safe_exit() {
    echo "[ERROR]: $1"
    docker compose down
    sudo rm -rf ./data
    rm -f ./app/employees.txt
    exit 1
}

step 1 "Top 10 CPU usage Processes"
top | head -n 17 || safe_exit "Failed to fetch top 10 CPU processes"

sleep 2

step 2 "Find and kill a process by name (e.g., telegram)."
pgrep -i Telegram | xargs kill || safe_exit "Failed to kill Telegram process."


sleep 2


step 3 "List all open network connections on your machine."
ss -tulnp || safe_exit "Failed to list open network connections."

sleep 2

step 4 "Monitor real-time disk usage with a command."
sudo iotop || safe_exit "Failed to monitor disk usage."

sleep 2

step 5 "Check memory usage and free system memory."
free -h || safe_exit "Failed to check memory usage."
