#!/usr/bin/python3

""" Script fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: %s" % type(html))
        print("\t- content: %s" % html)
        print("\t- utf8 content: %s" % html.decode("utf-8"))
