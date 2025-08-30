"""Given an integer, write a program to determine if its digits are in the
sorted order."""


def is_sorted(num):
    num_str = str(num)

    if len(num_str) < 3:
        return True

    is_desc = num_str[0] > num_str[1]

    for i in range(2, len(num_str)):
        if (num_str[i - 1] > num_str[i] and not is_desc) or (
            num_str[i - 1] < num_str[i] and is_desc
        ):
            return False

    return True
