#!/usr/bin/python3
"""A script that fetches a URL and displays the value of the X-Request-Id header."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    
    # Using the .get() method as required by your project's General instructions
    request_id = response.headers.get('X-Request-Id')
    
    if request_id is not None:
        print(request_id)
