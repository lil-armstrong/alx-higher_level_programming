#!/bin/bash
# Send a JSON POST request to a URL and display the response body
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1"
