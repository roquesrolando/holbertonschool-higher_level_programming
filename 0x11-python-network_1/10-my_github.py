#!/usr/bin/python3
"""prints ID of my github"""
import sys
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    passwd = sys.argv[2]
    response = requests.get(url, auth=(user, passwd))
    account = response.json()
    print(account.get('id'))
