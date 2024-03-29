#!/usr/bin/python3

"""
Script takes in a URL, sends a request to the URL \
    and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]

    if (len(args) < 1):
        print("Usage: %s <URL>" % (sys.argv[0]))
    else:
        try:
            url = args[0]
            r = requests.get(url)
            r.raise_for_status()
            print("%s" % (r.text))
        except requests.HTTPError as e:
            if e.response.status_code >= 400:
                print("Error code: %s" % (e.response.status_code))
