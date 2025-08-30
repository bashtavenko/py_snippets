"""Return the count of consecutive intervals consisting of equal numbers.

Example:  [3, 3, 3, 4, 2, 2, 4, 4] => 3

Part 2: There should never be more than one run for the same
number. For example: [3, 3, 4, 4, 1, 1] => 3
"""


def count_consecutive(data):
    """The simplest possible way."""
    result, prev_number, in_interval = 0, None, False

    for item in data:
        if item == prev_number:
            in_interval = True
        # Reason for elif - there could be different number
        # but if we are not in the interval, i.e. [1, 2, 3, 4]
        elif in_interval:
            in_interval = False
            result += 1
        prev_number = item

    return result + 1 if in_interval else result


def count_consecutive_2(data):
    """Similar to the first one but looks forward.
    This turns out to be more verbose because we need an index.
    """
    result, in_interval = 0, False
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            in_interval = True
        elif in_interval: # [1, 2, 3, 7, 5] => 0
            in_interval = False
            result += 1

    return result + 1 if in_interval else result


def count_consecutive_part2(data):
    # TODO: sort + binary search. Does not make sense.
    # If values on both sides are different, count it as an interval
    # But it would only work if group can have one member.
    # 1 1 3 3 4 4 4 7  => 3
    pass
