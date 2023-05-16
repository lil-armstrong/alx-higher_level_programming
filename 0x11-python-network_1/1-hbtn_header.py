#!/usr/bin/python3

""" Script takes in a URL, sends a request to the URL \
    and displays the value of the X-Request-Id variable \
        found in the header of the response. """

import sys
import urllib.request

if __name__ == "__main__":

    args = sys.argv[1:]

    if (len(args) < 1):
        print("Usage: %s <URL>" % (sys.argv[0]))

    url = args[0]
    with urllib.request.urlopen(url) as response:
        html = response.read()
        headers = response.headers
        print("%s" % (headers.get("X-Request-Id", None)))
