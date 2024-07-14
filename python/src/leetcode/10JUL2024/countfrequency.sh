#!/bin/bash

# Check if words.txt exists
if [ ! -f words.txt ]; then
  echo "File words.txt not found!"
  exit 1
fi

# Read the file, normalize spaces, split into words, and count frequencies
tr -s ' ' '\n' < words.txt | sort | uniq -c | sort -nr
