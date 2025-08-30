"""Polish notation PN calculator.

This is PN or Normal Polish Notation - NPN
+ 3 4
https://en.wikipedia.org/wiki/Polish_notation

* - 5 6 7 => (5 - 6) * 7
"""

import operator

OPS = {"-": operator.sub, "*": operator.mul, "/": operator.truediv, "+": operator.add}


def calculate_lor(str_exp):
    """Left to right calculator."""
    exp = tokenize(str_exp)
    ops, vals = [], []
    for token in exp:
        if token.isdigit():
            second = int(token)
            pending_val = False
            while pending_val and vals:
                first, op = int(vals.pop()), ops.pop()
                second = OPS[op](first, second)
            vals.append(second)
            pending_val = True  # Need another operand to complete expression
        elif token in OPS:
            ops.append(token)
            pending_val = False

    return vals.pop()


def calculate(str_exp):
    """Right to left calculator, much simpler."""
    exp = tokenize(str_exp)
    vals = []  # Only need one stack for operands (values)
    for token in reversed(exp):
        if token.isdigit():
            vals.append(int(token))
        elif token in OPS:
            first, second, op = vals.pop(), vals.pop(), token
            vals.append(OPS[op](first, second))
    return vals.pop()


def tokenize(str_exp):
    return str_exp.split(" ")
