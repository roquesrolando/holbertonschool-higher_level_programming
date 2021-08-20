#!/usr/bin/python3
"""Displays body and handles error"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
