#!/usr/bin/python3
"""
Script that prints GitHub user id using Basic Authentication.
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(
        url,
        auth=(username, password)
    )

    try:
        data = response.json()
        print(data.get("id"))
    except ValueError:
        print("None")
