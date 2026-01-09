#!/bin/bash

# Yoxla ki, subnetwork verilib ya yox
if [ -z "$1" ]; then
    echo "İstifadə: sudo $0 <subnetwork>"
    echo "Nümunə: sudo $0 192.168.1.0/24"
    exit 1
fi

# ARP scan ilə live hostları tap
sudo nmap -sn -PR "$1"
