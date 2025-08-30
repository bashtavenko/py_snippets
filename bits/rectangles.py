"""(4.11) Write a program to test if two rectangles have non-empty intersection.

Can be partial overlap, one contains the other, share common side, share common
corner, form a cross, tee, etc.

Better to test where rectangles do not intersect.
"""

import collections

Rectangle = collections.namedtuple("Rectangle", ("x", "y", "width", "height"))


def intersect_rectangles(r1, r2):
    def is_intersect(first, second):
        return (
            first.x <= second.x + second.width  # r2 left
            and first.x + first.width >= second.x  # r2 right
            and first.y <= second.y + second.height  # r2 top
            and first.y + first.height >= second.y
        )  # r2 bottom

    if not is_intersect(r1, r2):
        return Rectangle(0, 0, -1, -1)  # No intersection
    return Rectangle(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y),
    )
