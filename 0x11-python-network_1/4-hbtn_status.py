#!/usr/bin/python3

""" Script  fetches https://alx-intranet.hbtn.io/status.
"""

import requests

if __name__ == '__main__':

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)

    print("Body response:")
    print("\t- type: %s" % type(req.text))
    print("\t- content: %s" % req.text)
