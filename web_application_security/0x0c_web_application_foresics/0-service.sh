#!/bin/bash

LOG_FILE="auth.log"
if [ ! -f "$LOG_FILE" ]; then
    echo "Log file not found!"
    exit 1
fi
grep "pam_unix" "$LOG_FILE" | \
    grep -oP 'pam_unix\(\K[^:]+' | \
    sort | uniq -c | sort -nr | \
    head -n 1 | awk '{print $2}'
