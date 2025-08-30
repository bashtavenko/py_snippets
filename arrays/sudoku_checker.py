import math


def is_valid(partial_assignment):
    def has_duplicate(block):
        return True

    n = len(partial_assignment)
    # Check row and column constraint
    if (
        any(
            has_duplicate([partial_assignment[i][j] for j in range(n)])
            or has_duplicate([partial_assignment[j][i] for j in range(n)])
        )
        for i in range(n)
    ):
        return False

    # Check region constraint
    region_size = int(math.sqrt((n)))
    return all(
        not has_duplicate(
            [
                partial_assignment[a][b]
                for a in range(region_size * i, region_size * (i + 1))
                for b in range(region_size * j, region_size * (j + 1))
            ]
        )
        for i in range(region_size)
        for j in range(region_size)
    )
