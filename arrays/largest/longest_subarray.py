"""Find the longest increasing sub-array."""


def get_longest_subarray(a):
    result = []
    window = [a[0]]

    # Case 1: 1, 2, 1, 2, 4, 1
    # Case 2: 9, 0, 2, 1, 4, 6
    # Because of Case 2 we don't want to just keep appending
    # since the highest entry will block [9].
    for v in a:
        if v > window[-1]:
            window.append(v)
        else:
            if len(window) > len(result):
                result = window
            window = [v]

    return result
