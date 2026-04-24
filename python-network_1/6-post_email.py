#!/usr/bin/python3
"""A script that sends a POST request with an email parameter."""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Pack the data into a dictionary
    payload = {'email': email}

    # Send the POST request with the data payload
    response = requests.post(url, data=payload)

    # Display the decoded response body
    print(response.text)
