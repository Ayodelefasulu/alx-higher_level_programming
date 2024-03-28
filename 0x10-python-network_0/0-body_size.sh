#!/bin/bash

# Check if a URL argument is provided
if [ -z "$1" ]; then
  echo "Error: Please provide a URL as an argument."
  exit 1
fi

# Send request with curl and capture response with silent mode (-s)
response=$(curl -s "$1")

# Check if request was successful (exit code 0)
if curl -s "$1"; then
  # Extract body size using grep for "Content-Length" header and cut to get the number
  body_size=$(echo "$response" | grep -i 'Content-Length:' | cut -d':' -f2 | tr -d ' ')

  # Check if body size was found
  if [ -z "$body_size" ]; then
    echo "Body size not found in response."
  else
    echo "$body_size"
  fi
else
  echo "Error: Curl request failed."
  exit 1
fi

