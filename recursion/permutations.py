"""15.3 Generate permutations from array."""


def perm_backtracking(data):
    def gen_perm(i):
        if i==size:
            output.append("".join(a))
        else:
            for j in range(i, size):
                a[i], a[j] = a[j], a[i]
                gen_perm(i + 1)
                a[i], a[j] = a[j], a[i]  # Reached the bottom, backtrack

    output = []
    a = list(data)
    size = len(a)
    gen_perm(0)
    return output
