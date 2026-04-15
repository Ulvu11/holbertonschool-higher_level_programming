#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print("{:d}".format(i))
            count += 1
    except Exception:
        continue

    return count
