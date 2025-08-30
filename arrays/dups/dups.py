"""Delete dups from a sorted array."""


def delete_dups_brute_force(a):
    def shift(i, j, a):
        for x in range(i, j):
            a[x] = a[x + 1]

    size = len(a)
    i, j = 0, size - 1
    # No dups to the left of i. We haven't seen elements to the right.
    # j is end of non-zero portion
    while i < j:
        while a[i + 1]==a[i]:
            shift(i, j, a)
            a[j] = 0
            j -= 1
        i += 1


def delete_dups(a):
    """Array is sorted.
    Need two indexes, one is to iterate and another for write.
    Write only if not dup. This only works in sorted array.
    """
    write_index = 1
    for i in range(1, len(a)):
        if a[write_index - 1]!=a[i]:
            a[write_index] = a[i]
            write_index += 1

    for i in range(write_index, len(a)):
        a[i] = 0
