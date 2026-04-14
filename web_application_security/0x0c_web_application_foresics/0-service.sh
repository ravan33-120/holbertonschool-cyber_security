#!/bin/bash
grep -oP '(?<=sshd\[)\d+' /var/log/auth.log 2>/dev/null || \
awk '{print $6}' /var/log/auth.log | sort | uniq -c | sort -rn
