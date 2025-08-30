"""Searching bootcamp."""

import bisect
import collections


def binary_search_i(a, value):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if value < a[mid]:  # Must be somewhere on the left
            hi = mid - 1
        elif value > a[mid]:  # Must be somewhere on the right
            lo = mid + 1
        else:
            return mid

    # No exact match
    # Lo very well may end up being > hi (mid + 1)
    return lo


def binary_search_r(a, value):
    def search_r(lo, hi):
        if lo >= hi:
            return lo

        mid = lo + (hi - lo) // 2
        if value < a[mid]:
            return search_r(lo, mid - 1)
        elif value > a[mid]:
            return search_r(mid + 1, hi)
        else:
            return mid

    return search_r(0, len(a))


Student = collections.namedtuple("Student", ("name", "gpa"))


def search_student(students, target):
    def comp_gpa(student):
        return student.gpa, student.name

    # Find a position in the list where new element will be inserted in order to
    # keep list sorted.
    # _left first element less than target
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    print(i)
    # I don't understand what that means.
    return 0 <= i < len(students) and students[i]==target
