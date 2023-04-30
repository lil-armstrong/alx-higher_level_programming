#!/bin/bash
SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo "Size of the response body: $SIZE bytes"
