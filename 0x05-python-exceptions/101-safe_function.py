#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        safe_func = fct(*args)
    except (TypeError, NameError, ZeroDivisonError, IndexError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return safe_func
