"""11.1 Search array for first occurrence of k.

Twist - there are duplicates
[-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
108: 3
"""


def search(data, k):
    lo, hi, result = 0, len(data), -1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if k < data[mid]:
            hi = mid - 1
        elif k > data[mid]:
            lo = mid + 1
        else:
            result = mid
            hi = mid - 1  # This is the only twist - don't look to the right

    return result


if __name__=="__main__":
    a = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    print(search(a, 108))
    print(search(a, 285))
    print(search(a, 109))
