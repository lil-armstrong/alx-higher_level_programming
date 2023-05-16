#!/usr/bin/python3

""" Script takes in a URL, sends a request to the URL \
    and displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.request

if __name__ == '__main__':

    args = sys.argv[1:]

    if (len(args) < 2):
        print("Usage: %s <URL>" % (sys.argv[0]))
    else:
        try:
            url = args[0]
            req = urllib.request.Request(url)

            with urllib.request.urlopen(req) as response:
                html = response.read().decode("utf-8")
                print(html)
        except urllib.error.URLError as e:
            print("Error code: %s" % e.code)
