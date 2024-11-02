#!/usr/bin/python3
# Prints names defined by compiled module hidden_4.pyc
# This required python3.8
# The hidden_py file was compiled with python3.8

if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    # Alternative code can be subsituted here

    for f in sorted(name):
        if f.startswith('__'):
            continue
        else:
            print(f)
    """
    This is an alternative code


    sorted_name = sorted(f for f in name if not f.startswith('__'))
    for test in sorted_name:
        print(test)


    """
