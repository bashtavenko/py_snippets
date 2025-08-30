"""Given a secret word and a guess word return how close the guess is."""

import collections


def score_word(secret, guess):
    """Score the guess without repetitions in either secret or guess.
    Map of secret, Looping over guess.
    """

    secret_map = {}
    for i, char in enumerate(secret):
        secret_map[char] = i

    output = ""
    for i, char in enumerate(guess):
        if char in secret_map:
            if i==secret_map[char]:
                output += "G"
            else:
                output += "Y"
        else:
            output += "R"
    return output


def score_word_with_repetitions(secret, guess):
    """Scores the guess with repeitions in either guess or secret."""

    char_frequency = collections.Counter(secret)
    secret_map = collections.defaultdict(set)
    for i, char in enumerate(secret):
        secret_map[char].add(i)

    output = ""
    # Find characters in correct positions
    green_positions = set()
    yellow_positions = set()
    for i, char in enumerate(guess):
        if i in secret_map[char]:
            green_positions.add(i)
            char_frequency[char] -= 1

    # Take care of the rest
    for i, char in enumerate(guess):
        if i in green_positions:
            continue
        if char in secret_map and char_frequency[char] > 0:
            char_frequency[char] -= 1
            yellow_positions.add(i)

    # Build back
    for i in range(0, len(guess)):
        if i in green_positions:
            output += "G"
        elif i in yellow_positions:
            output += "Y"
        else:
            output += "R"

    return output
