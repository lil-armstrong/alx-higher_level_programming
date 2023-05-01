#!/bin/bash
# Send curl request and capture HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1")
