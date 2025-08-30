"""Dutch national flag."""


def dutch(a):
    """Dutch national flag partitioning.

    Need <V = V  >V, but elements less or greater V are not sorted.
    """
    # Three pointers: lt - less, gt - greater, i - equal
    # It just a matter of moving i across while maintaining
    # these three invariants.

    # This is a bit more complicated that Quick Sort partitioning
    # where we don't need an equal zone
    lt, gt, i = 0, len(a) - 1, 1
    v = a[i]
    while i <= gt:
        if a[i] < v:
            # Whatever less than equal(i) should be LEFT os
            # of i. If not, exchange and move lt and i
            # because equal needs to be adjusted
            a[i], a[lt] = a[lt], a[i]
            lt, i = lt + 1, i + 1
        elif a[i] > v:
            # Whatever is greater than equal(i) should be
            # RIGHT, if not, exchange and adjust gt
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:  # ==
            # Equal zone, keep going
            i += 1

    return lt, gt, i
