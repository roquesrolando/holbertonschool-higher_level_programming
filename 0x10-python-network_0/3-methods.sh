#!/bin/bash
# Write a Bash script that displays all HTTP methods
curl -sI "$1" | grep -i Allow | cut -d ' ' -f 2-
