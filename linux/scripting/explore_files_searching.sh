#!/bin/bash

# Find the absolute path of the bash shell.
echo Absolute path of bash: $(which bash)

# Search for the word "error" in a system log file.
grep "error" /var/log/syslog

# Count the number of lines in a file (e.g., /etc/passwd).
wc -l /etc/passwd

# Display only the first 10 lines of /etc/passwd.
# by default head shows 10, so i'll show 11 
head -n 11 /etc/passwd

# Show only the last 5 lines of /etc/passwd.
echo ------------ TAIL WAALA -----------
tail -n 5 /etc/passwd
