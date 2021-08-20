#!/usr/bin/python3
"""
Takes in a web and an email, sends a POST request to the passed web with the
email as a parameter, and displays the body of the response (decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    web = sys.argv[1]
    mail = urllib.parse.urlencode({'email': sys.argv[2]})
    mail = mail.encode('utf8')
    with urllib.request.urlopen(web, mail) as response:
        print(response.read().decode('utf8'))
