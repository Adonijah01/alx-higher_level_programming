#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as thefirst argument, and displays the body of the response.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
