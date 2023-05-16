#!/usr/bin/python3

"""
Script takes 2 arguments in order to solve a challenge
"""

if __name__ == "__main__":
    import requests
    import sys

    args = sys.argv[1:]

    if len(args) < 2:
        print("Usage %s <GIT REPO NAME> <GIT OWNER NAME>")
    else:
        try:
            repo = args[0]
            owner = args[1]
            url = " https://api.github.com/repos/%s/%s/commits" % (owner, repo)
            headers = {
                'X-GitHub-Api-Version': '2022-11-28',
                "Accept": "application/vnd.github+json"
            }

            response = requests.get(url, headers=headers,
                                    params={'per_page': 10})
            commits = response.json()
            for commit in commits:
                print('%s: %s' % (commit.get("sha", ""),
                                  commit["commit"]["author"]["name"]))
        except ValueError as e:
            print(e)
