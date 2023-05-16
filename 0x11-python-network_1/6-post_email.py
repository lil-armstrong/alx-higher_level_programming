#!/usr/bin/python3

"""
Script takes in a URL and an email address, \
    sends a POST request to the passed URL\
        with the email as a parameter, \
            and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]

    if (len(args) < 1):
        print("Usage: %s <URL> <EMAIL>" % (sys.argv[0]))
    else:
        url = args[0]
        email = args[1]
        payload = {
            "email": email
        }
        r = requests.post(url, data=payload)
        print("%s" % (r.text))
