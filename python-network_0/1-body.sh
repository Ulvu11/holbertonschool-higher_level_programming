#!/bin/bash
#Sends a GET request to a URL and displays the body only if the status code is 200
curl -sL -w "%{http_code}" "$1" -o /tmp/body_out | grep -q "200" && cat /tmp/body_out
