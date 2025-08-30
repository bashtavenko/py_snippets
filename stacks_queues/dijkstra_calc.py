"""Dijkstra two-stack algorithm for expression evaluation.
"""


def evaluate(exp):
    OPS = {
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "+": lambda x, y: x + y,
    }

    ops, vals = [], []
    for c in exp:
        if c == "(":
            continue
        elif c in OPS:
            ops.append(c)
        elif c == ")":
            op = ops.pop()
            x, y = vals.pop(), vals.pop()
            vals.append(OPS[op](x, y))
        else:
            vals.append(int(c))
    return vals.pop()
