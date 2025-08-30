"""6.4 Replace and remove.

1. Replace each 'a' by two d's.
2. Delete each entry containing 'b'

[a, c, d, b, b, c, a] => [d, d, c, d, c, d, d]
"""


def replace_and_remove(s):
    write_index, a_count = 0, 0
    size = len(s)

    for i in range(size):
        if s[i] != "b":
            # Delete "b"
            s[write_index] = s[i]
            write_index += 1
        if s[i] == "a":
            # "a" => "dd"
            a_count += 1

    cur_index = write_index - 1
    write_index += a_count - 1
    final_size = write_index + 1
    while cur_index >= 0:
        if s[cur_index] == "a":
            s[write_index - 1 : write_index + 1] = "dd"
            write_index -= 2
        else:
            s[write_index] = s[cur_index]
            write_index -= 1
        cur_index -= 1
    return final_size
