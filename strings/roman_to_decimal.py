import functools


def roman_to_decimal(s):
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    f = lambda val, i: (val + -T[s[i]]
                        if T[s[i]] < T[s[i + 1]]
                        else T[s[i]])

    # reduce - apply function of two arguments to each element of iterator
    return functools.reduce(f,
            reversed(range(len(s) - 1)), # Reversed is built-in
            T[s[-1]])
