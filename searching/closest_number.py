"""Find number closest to the given number in the array(trivial).
Without BS we'd have to check every single point which would be O(n)
but BS would run in O(log(n) although if we start empty, we could
maintain an array in sorted order by doubling it.

It would be a lot more interesting to find or counts points in the range
 (1d-range search) for which we would need either BS twice or
BST with range search.
"""


def find_number(data, n):
    data = sorted(data)
    lo, hi = 0, len(data)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if n < data[mid]:
            hi = mid - 1
        elif n > data[mid]:
            lo = mid + 1
        else:
            return data[mid]

    # TODO: Check lo or hi is out ot bound and also wrong
    return data[lo] if abs(n - data[lo]) < abs((data[hi] - n)) else data[hi]


def find_number_r(data, n):
    def find(lo, hi):
        if lo >= hi:
            return data[lo] if abs(n - data[lo] < abs((data[hi] -n))) else data[hi]

        mid = lo + (hi - lo) // 2
        if n < data[mid]:
            return find(lo,  mid - 1)
        elif n > data[mid]:
            return find(mid + 1, hi)
        else:
            return data[mid]

    data = sorted(data)
    return find(0, len(data))


if __name__ == '__main__':
    print (find_number([3, 1, 7, 5, 12, 4, 8, 24], 11))
    print (find_number_r([3, 1, 7, 5, 12, 4, 8, 24], 11))
    print (find_number([1, 3, 4, 5, 7, 8, 12, 24], 9))
    print (find_number_r([1, 3, 4, 5, 7, 8, 12, 24], 9))
    print (find_number([1, 3, 4, 5, 7, 8, 12, 24], 23))
    print (find_number_r([1, 3, 4, 5, 7, 8, 12, 24], 23))
    print (find_number([1, 3, 4, 5, 7, 8, 12, 24], 5))
    print (find_number_r([1, 3, 4, 5, 7, 8, 12, 24], 5))