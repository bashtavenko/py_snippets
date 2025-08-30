"""18.7 Checks if string 's' can be transformed or produced into string 't'.

Replace one character at time to any other character such as resulted string
will be in the dictionary.

Production sequence for the dictionary

'bat', 'cot', 'dog', 'dag', 'dot', 'cat' is

cat -> cot -> dot -> dog

This is almost stock BFS, BFS is because we need the shortest path.
"""

import collections
import string

StringWithDistance = collections.namedtuple(
    "StringWithDistance", ("candidate_string", "distance")
)


def transform_string(d, s, t):
    """Returns the number of steps to reach a string.

    Args:
      d: dictionary
      s: source string
      t: destination string
    Returns:
     Number of steps.
    """
    q = collections.deque([StringWithDistance(s, 0)])

    # As a shortcut we remove string from the dictionary instead of having
    # 'marked' set
    d.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string==t:
            return f.distance  # Number of steps to reach t

        # We don't have adjacency list here
        for i in range(len(f.candidate_string)):
            for (
                c
            ) in string.ascii_lowercase:  # Or we could simply define const 'abcde...'
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in d:  # if not marked
                    d.remove(cand)  # Mark
                    q.append(StringWithDistance(cand, f.distance + 1))

    return -1
