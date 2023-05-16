#!/usr/bin/python3

""" Script takes in a URL and an email, sends a POST request\
    to the passed URL with the email as a parameter, and \
        displays the body of the response (decoded in utf-8) """

import sys
import urllib.request

if __name__ == "__main__":

    args = sys.argv[1:]

    if (len(args) < 1):
        print("Usage: %s <URL> <EMAIL>" % (sys.argv[0]))
    else:
        url = args[0]
        email = args[1]
        payload = {
            "email": email
        }
        data = urllib.parse.urlencode(payload)
        data = data.encode('ascii')
        req = urllib.request.Request(url, data, method="POST")

        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8")
            print("%s" % (html))
