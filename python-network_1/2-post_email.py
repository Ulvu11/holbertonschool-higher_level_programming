#!/usr/bin/python3
"""This module sends a POST request with an email and prints the r. body"""

import sys
import urllib.request
import urllib.parse


def post_email(url, email):
    """Send a POST request with the email parameter and print the response"""
    data = urllib.parse.urlencode({"email": email})
    data = data.encode("utf-8")
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode("utf-8")
        print(body)


def main():
    """Get the URL and email from the command line and send the request"""
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)


if __name__ == "__main__":
    main()
