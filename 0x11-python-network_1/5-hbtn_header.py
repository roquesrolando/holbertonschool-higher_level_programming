#!/usr/bin/python3
"""Displays header of URL"""
import sys
import requests


if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    b_dict = response.headers
    print(b_dict.get('X-Request-Id'))
