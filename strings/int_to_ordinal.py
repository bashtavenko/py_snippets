"""Convert int to an ordinal string.

0  th
1  1st
2  2nd
3  3rd
4  4th
10 10th
21 21st
"""


def convert_int_to_ordinal(n):
    suffixes = ["th", "st", "nd", "rd"] + ["th"] * 6
    return str(n) + suffixes[n % 10]


if __name__=="__main__":
    print(convert_int_to_ordinal(2))
    print(convert_int_to_ordinal(21))
    print(convert_int_to_ordinal(33))
