#!/usr/bin/python3

"""
 Script takes your GitHub credentials (username and password) 
 and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import requests
    import sys

    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage: %s <GITHUB USERNAME> <GITHUB PASSWORD>" % (sys.argv[0]))

    else:
        try:
            username = args[0]
            secret = args[1]
            url = "https://api.github.com/user"
            headers = {
                'X-GitHub-Api-Version': '2022-11-28',
                "Accept": "application/vnd.github+json",
            }
            auth = (username, secret)
            response = requests.get(url, headers=headers, auth=auth)
            data = response.json()

            print(data.get("id", ""))
        except ValueError as e:
            print(e)
