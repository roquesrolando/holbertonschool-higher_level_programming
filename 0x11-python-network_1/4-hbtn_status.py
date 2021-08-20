#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    content = response.content.decode('utf8)')
    print("Body response:\n\t- type: {}\n\t- content: {}".format(type(content),
          content))
