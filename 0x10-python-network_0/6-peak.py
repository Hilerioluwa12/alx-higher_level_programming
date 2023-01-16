#!/usr/bin/python3
""" find the peak
"""


def recursion(begin, last, k):
    """ search
    """
    mid = (begin + last)

    if (mid % 2 == 0):
        m = int(mid / 2)
    else:
        m = int((mid - 1) / 2)
    if (m == 0 or k[m] >= k[m - 1]) and (m == last - 1 or k[m] >= k[m + 1]):
        return (k[m])
    elif (m > 0 and k[m] < k[m - 1]):
        return (recursion(begin, m, k))
    elif (m < last - 1 and k[m] < k[m + 1]):
        return (recursion(m, last, k))
    else:
        return(None)


def find_peak(list_of_integers):
    """ function that get the peak from a list
    """
    if not list_of_integers:
        return (None)

    i = list_of_integers
    return (recursion(0, len(i), i))
