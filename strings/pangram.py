"""Given a sentence, check if it's a pangram."""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def is_pangram(phrase):
    for char in ALPHABET:
        if char not in phrase:
            return False

    return True


def is_pangram_set(phrase):
    return not (set(ALPHABET) - set(phrase))
