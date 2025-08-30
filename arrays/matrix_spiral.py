"""5.18 Compute the spiral ordering of a 2D array.

1  2  3
4  5  6
7  8  9

Should be 1, 2, 3, 6, 9, 8, 7

zip(*m) unpack tuple and zip it
  m = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
  zip(*m) = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
      *m = unpacks tuple into positional argument
           just needed for zip()
  So, zip(*m) transposes the matrix
zip((1, 2, 3), (4, 5, 6), (7, 8, 9))
"""


def matrix_in_spiral(m):
    def matrix_layer(offset):
        if offset==len(m) - offset - 1:
            # Corner case of odd dimension matrix with last iteration.
            # We just need one element.
            out.append(m[offset][offset])
            return

        # row: first n - 1 cells
        out.extend(m[offset][offset: -1 - offset])  # forward
        # transpose, column: n - 1 last cell
        out.extend(list(zip(*m))[-1 - offset][offset: -1 - offset])  # transpose
        # row: last n - 1 cells in reverse order (::-1)
        out.extend(m[-1 - offset][-1 - offset: offset: -1])  # reverse
        # transpose, column n - 1 in reversed order
        out.extend(list(zip(*m))[offset][-1 - offset: offset: -1])

    out = []
    for o in range(len(m) + 1 // 2):
        matrix_layer(o)
    return out
