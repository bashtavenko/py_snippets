"""Find the closest point to the given one in the list of points.

For example: given 5 points (1, 1), (1, 2), (2, 4), (3, 1), (4, 3)
             and position (4, 1), the answer is (3, 1)
"""
import collections
import sys
import math

Point = collections.namedtuple('Point', ('x', 'y'))


def get_closest(points, position):
    min_sofar, curr_distance = sys.maxsize, sys.maxsize
    min_point_sofar = None
    for point in points:
        curr_distance = math.sqrt((point.x - position.x) ** 2 +
                                  (point.y - position.y) ** 2)
        if min_sofar > curr_distance:
            min_sofar = curr_distance
            min_point_sofar = point

    return min_point_sofar


if __name__ == '__main__':
    points = [Point(1, 1),
              Point(1, 2),
              Point(2, 4),
              Point(3, 1),
              Point(4, 3)]
    print (get_closest(points, Point(4, 1)))
    print (get_closest(points, Point(2, 2)))