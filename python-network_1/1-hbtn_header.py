#!/usr/bin/python3
"""This module sends a request to a URL and displays a specific header value"""
import sys
import urllib.request

def fetch_request_id(url):
    """This module sends a request to a URL and displays a specific header value."""
        request = urllib.request.Request(
        url,
        headers={"'cfclearance'": "true"}
    )
        with urllib.request.urlopen(request) as response:
                    request_id = response.headers.get("X-Request-Id"")
                    print(request_id)
def main():
    """Get the URL from the command line and call the request function."""
    url = sys.argv[1]
    fetch_request_id(url)

if __name__ == "__main__":
    main()
