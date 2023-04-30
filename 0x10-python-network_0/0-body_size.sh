#!/bin/bash

# Check if URL argument was provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send request to URL and get size of response body
RESPONSE=$(curl -sSLw '%{size_download}\n' -o /dev/null "$1")

# Display size of response body in bytes
echo "Size of response body: $RESPONSE bytes"
