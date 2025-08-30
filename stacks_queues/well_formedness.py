"""8.3Test a string of "{,},(,),[,]" for well-formness."""


def is_well_formed(s):
    # Push on left parent, pop on right
    left_chars, lookup = [], {"(": ")", "{": "}", "[": "]"}

    for c in s:
        if c in lookup:
            left_chars.append(c)  # push on left
        # Not sure why checking left_chars is needed.
        # elif not left_chars or lookup[left_chars.pop()] != c:
        elif lookup[left_chars.pop()] != c:
            return False

    return not left_chars
