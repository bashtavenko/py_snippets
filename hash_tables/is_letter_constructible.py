"""12.2 Is an anonymous letter constructable?

Is it possible to create a letter from the given magazine source?

"""

import collections


def is_letter_constructable(letter_text, magazine_text):
    freq_letter = collections.Counter(letter_text)

    for c in magazine_text:
        if c in freq_letter:
            freq_letter[c] -= 1
            if freq_letter[c]==0:
                del freq_letter[c]
                if not freq_letter:
                    return True

    return not freq_letter


def is_letter_constructable_pythonic(letter_text, magazine_text):
    """Pythonic solution with Counter() - Counter()."""
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)
