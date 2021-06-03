#!/usr/bin/python3

def save_to_json_file(my_obt, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(my_obt, f)
