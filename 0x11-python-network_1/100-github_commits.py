#!/usr/bin/python3
"""Use github APi for list the 10 las commit in user and repo given."""
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    req = requests.get(url)
    try:
        for i in range(10):
            print("{}: {}".format(req.json()[i].get("sha"),
                                  req.json()[i].get("commit").
                                  get("author").get("name")))
    except IndexError:
        pass
