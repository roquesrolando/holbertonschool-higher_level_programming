#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(err), file=sys.stderr)
        return False
