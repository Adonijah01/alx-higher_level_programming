#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) """
import urllib.request
import sys
import urllib.parse
