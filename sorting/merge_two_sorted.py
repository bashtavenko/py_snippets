""" 13.2 Merge two sorted arrays.
1. Iterator is better than index
2. Keep pulling from and array until it's less
"""


def merge_arrays_ugly(a, b):
    result = []
    it_a, it_b = iter(a), iter(b)

    first = next(it_a, None)
    second = next(it_b, None)
    # "is not None" in case the value is 0
    while first is not None and second is not None:
        if first < second:
            result.append(first)
            first = next(it_a, None)
        elif first > second:
            result.append(second)
            second = next(it_b, None)
        else:
            result.append(first)
            first = next(it_a, None)
            second = next(it_b, None)

    # Pull remaining
    while first is not None:
        result.append(first)
        first = next(it_a, None)

    while second is not None:
        result.append(second)
        second = next(it_b, None)

    return result


# Cute but the problem is:
# a) mutates lists; b) doesn't run in O(n) because of pop()
def merge_arrays(a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    return result + a + b
