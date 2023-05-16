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
        repo = args[0]
        owner = args[1]
        url = " https://api.github.com/repos/%s/%s/commits" % (repo, owner)
        headers = {
            'X-GitHub-Api-Version': '2022-11-28',
            "Accept": "application/vnd.github+json"
        }
        auth = ("lil-armstrong", "github_pat_11AHPGKRY03" +
                "Etw2izLsNE6_BL9SBOiwyrIRXPebqSXDem2yH6wnTy5" +
                "m0JygeuL4be4DAMKP64MPVp5Y104")
        response = requests.get(url, headers=headers,
                                auth=auth, params={'per_page': 10})
        commits = response.json()
        for commit in commits:
            print('%s: %s' % (commit.get("sha", ""),
                  commit["commit"]["author"]["name"]))
