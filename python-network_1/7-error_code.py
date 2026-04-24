#!/usr/bin/python3
"""A script that fetches a URL and handles HTTP errors using requests."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Send the GET request
    response = requests.get(url)

    # Check if the status code is an error (400 or higher)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
