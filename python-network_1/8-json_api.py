#!/usr/bin/python3
"""Script that sends a POST request to search for users by letter"""

import requests
import sys


if __name__ == "__main__":
    # Get the letter from command line argument
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # API endpoint
    url = "http://0.0.0.0:5000/search_user"

    # Data to send in POST request
    data = {'q': letter}

    try:
        # Send POST request
        response = requests.post(url, data=data)

        try:
            # Try to parse JSON response
            json_data = response.json()

            # If JSON is empty
            if not json_data:
                print("No result")
            else:
                # Print id and name
                print("[{}] {}".format(
                    json_data.get('id'),
                    json_data.get('name')
                ))

        except ValueError:
            # If response is not valid JSON
            print("Not a valid JSON")

    except requests.exceptions.RequestException:
        # Handle request errors
        print("Request failed")
