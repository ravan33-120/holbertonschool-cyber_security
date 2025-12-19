#!/bin/bash
echo $(cat /dev/urandom | tr -dc '[:alnum:]' |  head -c $1)
