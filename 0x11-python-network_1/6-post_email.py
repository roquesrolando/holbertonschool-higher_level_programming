#!/usr/bin/python3
"""Sends a POST request with he email"""
import sys
import requests


if __name__ == '__main__':
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.content.decode('utf8'))
