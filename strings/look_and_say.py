"""Look-and-say.
   1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
   1 => one 1 => 11
   11 => two 1s => 21
   21 => one 2, one 1 => 1211
   1211 => one 1, one 2, two ones => 111221
   111221 => three ones, 2 twos, one ones 312211
   312211 => 13112221
   13112221 => 1113213211

   Generate verbiage for the number of given length
"""
import itertools


def look_and_say(n):
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return ''.join(result)

    s = '1'
    for _ in range(n - 1):
        s = next_number(s)

    return s


def look_and_say_groupby(n):
    """GroupBy version

    Itertools group by works on consecutive characters and
    starts a new group when value changes

    for x, y in itertools.groupby('111221'):
        print x, list(y)

    1 ['1', '1', '1']
    2 ['2', '2']
    1 ['1']
    """
    def next_number(s):
        return ''.join(
            str(len(list(group))) + key for key, group in itertools.groupby(s))

    s = '1'
    for _ in range(n - 1):
        s = next_number(s)

    return s
