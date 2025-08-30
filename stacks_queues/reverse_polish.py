"""8.2 Reverse Polish notation RPN calculator.

This is RPN or Reverse Polish Notation - RPN
3 4 +
"""

import operator


def evaluate(rpn_expression):
    DELIMITER = " "
    OPS = {
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "+": operator.add,
    }

    vals = []

    for token in rpn_expression.split(DELIMITER):
        if token in OPS:
            vals.append(OPS[token](vals.pop(), vals.pop()))
        else:  # Token is a number
            vals.append(int(token))
    return vals[-1]
