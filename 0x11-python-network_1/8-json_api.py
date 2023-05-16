#!/usr/bin/python3

"""
Script takes in a letter and sends a POST \
    request to http://0.0.0.0:5000/search_user \
        with the letter as a parameter
"""

if __name__ == '__main__':
    import requests
    import sys

    class NoResultException(Exception):
        pass

    args = sys.argv[1:]

    if len(args):
        value = args[0]
    else:
        value = ""

    try:
        payload = {'q': value}
        url = 'http://0.0.0.0:5000/search_user'

        r = requests.post(url, data=payload)
        data = r.json()

        if len(data) < 1:
            raise NoResultException("No result")
        print("[%s] %s" % (data.get("id", ""), data.get("name", "")))
    except ValueError as e:
        print("Not a valid JSON")
    except NoResultException as e:
        print(str(e))
