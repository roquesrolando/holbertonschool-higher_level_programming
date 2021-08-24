#!/bin/bash
# displays the size of the body of URL
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
