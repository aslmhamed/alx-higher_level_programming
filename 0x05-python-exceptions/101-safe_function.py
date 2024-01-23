#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        safe_func = fct(*args)
    except (TypeError, NameError, ZeroDivisionError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return safe_func
