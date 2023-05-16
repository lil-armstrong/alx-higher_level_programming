#!/usr/bin/python3

""" Script  fetches https://alx-intranet.hbtn.io/status.
"""

import requests
import sys

if __name__ == '__main__':
    args = sys.argv[1:]

    if (len(args) < 1):
        print("Usage: %s <URL>" % (sys.argv[0]))
    else:
        url = args[0]
        req = requests.get(url)
        headers = req.headers
        print("%s" % (headers.get("X-Request-Id", None)))
