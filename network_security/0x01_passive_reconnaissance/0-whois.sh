#!/bin/bash

whois "$1" | awk -F: '
/^(Registrant|Admin|Tech)/ {
  field=$1
  value=$2

  # Street üçün axırda space
  if (field ~ /Street/) value=value " "

  # Ext sahələri üçün : qorunur
  if (field ~ /Ext/) field=field ":"

  # Boş value üçün CSV saxla
  if (value == "") value=""

  print field "," value
}
' > "$1.csv"

