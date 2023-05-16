#!/usr/bin/python3

"""
Script takes in a letter and sends a POST request \
    to http://0.0.0.0:5000/search_user with the letter as a parameter"""

if __name__ == '__main__':
    import requests
    import sys

    args = sys.argv[1:]

    if len(args) < 1:
        value = ""
    else:
        value = args[0]

    try:
        payload = {'q': value}
        url = 'http://0.0.0.0:5000/search_user'

        r = requests.post(url, json=payload)
        data = r.json()

        print("[%s] %s" % (data.id, data.name))
    except requests.exceptions.InvalidJSONError as e:
        print("Not a valid JSON")
    except requests.exceptions.JSONDecodeError as e:
        print("No result")
