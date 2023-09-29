#!/usr/bin/python3
"""
Sript that takes in a URL, sends a request\
        to the URL and displays the value of\
        the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        headers = response.getheaders()
        header_dict = dict(headers)
        request_id = header_dict.get('X-Request-Id')
        print(request_id)
        pass
