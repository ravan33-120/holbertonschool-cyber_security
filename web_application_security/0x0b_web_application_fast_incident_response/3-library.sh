#!/bin/bash


LOGFILE="logs.txt"


# Step 1: Find attacker IP (most frequent IP address)

attacker_ip=$(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$LOGFILE" | sort | uniq -c | sort -rn | head -n1 | awk '{print $2}')

# Step 2: Filter log lines by attacker IP, extract User-Agent string (field 12), count, and get most frequent#

grep "^$attacker_ip " "$LOGFILE" \
  | awk -F\" '{print $6}' \
  | sort | uniq -c | sort -rn | head -n1 \
  | awk '{print $2}'

