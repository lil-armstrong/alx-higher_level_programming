#!/usr/bin/python3

""" Script  fetches https://alx-intranet.hbtn.io/status.
"""

import requests

if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    headers = req.headers
    print("%s" % (headers.get("X-Request-Id", None)))
