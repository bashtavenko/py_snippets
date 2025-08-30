"""Generates all possible combinations of 1 and 0 for n bits.

1 => 0, 1
2 => 00,01,10,11
3 => 000, 001, 010, 011, ...
Cannot use any mathematical operators

It backtracks by unwinding stack, i.e.
if n == 1:
  data[n - 1] = 0
  print data

  data[n - 1] = 1
  print data
"""


def generate(n):
    """Generates bit permutations of n length.

    Very similar to permutations.py except it generates permutations
    instead of permuting a given array
    """

    def generate_helper(n):
        if n==0:
            result.append("".join(str(s) for s in data))
        else:
            data[n - 1] = 0
            generate_helper(n - 1)
            # Reached the bottom, backtrack
            data[n - 1] = 1
            generate_helper(n - 1)

    data = [0] * n
    result = []
    generate_helper(n)
    return result
