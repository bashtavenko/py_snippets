"""16.2 Levenshtein distance.

Minimum number of edits it would take to transform the misspelled word into correct word

Saturday -> Sunday is 4
1. Delete fist 'a' and 't' (2)
2. Change 'r' to 'n'       (1)
3. Insert trailing 's'     (1)

Essentially, go from the back and determine which of these three choices
would be better when looking at the last characters of strings:
- move both (go to the next char in both strings)
- move first
- move second
"""

def levenshtein_distance(a, b):
    """Computes edit distance."""
    def compute_distance(a_index, b_index):
        if a_index < 0:
            return b_index + 1  # add all b's
        elif b_index < 0:
            return a_index + 1 # delete all a's

        if distance[a_index][b_index] == -1:
            if a[a_index] == b[b_index]:
                distance[a_index][b_index] = (
                    compute_distance(a_index - 1, b_index - 1))
            else:
                move_both = compute_distance(a_index - 1, b_index -1)
                move_first = compute_distance(a_index - 1, b_index)
                move_second = compute_distance(a_index, b_index - 1)
                distance[a_index][b_index] = (
                        1 + min(move_both, move_first, move_second))

        return distance[a_index][b_index]

    distance = [[-1] * len(b) for _ in a]
    return compute_distance(len(a) - 1, len(b) - 1)

