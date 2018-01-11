import random


def bin_search(values, x):

    low = 0
    high = len(values) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if x < v[mid]:
            high = mid - 1
            mid = mid - 1
        elif x > v[mid]:
            low = mid + 1
        else:
            return mid

    return -1
    