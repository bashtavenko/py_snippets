"""15.4 Power set."""


def power_set_bits(input_set):
    """Method 1 - use bit array
    00
    01 take first
    10 take second
    11 take both
    """
    power_set = []
    size = len(input_set)

    # range(1 << 2) [0, 1, 2, 3]
    # range(1 << 3) [0, 1, 2, ... 7]
    for i in range(1 << size):  # Fancy way of 2 ** size
        sub_set = ""
        for j in range(size):
            if (i & (1 << j)) > 0:
                sub_set += input_set[j]

        power_set.append("".join(sub_set))

    return power_set


def generate_powerset(input_set):
    """
    Method 2 - recursion.
    ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
    """

    def generate(i, sub_set):
        if i==len(input_set):
            power_set.append(sub_set)
        else:
            generate(i + 1, sub_set)
            generate(i + 1, sub_set + input_set[i])

    power_set = []
    generate(0, "")
    return power_set
