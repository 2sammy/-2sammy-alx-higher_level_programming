#!/usr/bin/python3

"""
A script that takes in a URL and sends a reque

    and displays the body of the response deco

    urllib.error.HTTPError is managed and prin

    Error code: <HTTP status code>
"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as re
            html = resp.read()
            print("{}".format(html.decode('utf
    except urllib.error.HTTPError as e:

