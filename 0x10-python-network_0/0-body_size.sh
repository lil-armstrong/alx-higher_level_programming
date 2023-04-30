#!/bin/bash
# Ge tthe byte size of a curl request
curl -s "$1" | wc -c
