""" 6.6 Reverse all words in a sentence.

Alice likes Bob => Bob likes Alice

Reverse all characters and then reverse each word
012345678
boB sekil ecilA
"""


def reverse(s):
    def reverse_all():
        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]

    def reverse_one(lo, hi):
        size = hi - lo + 1
        for i in range(size // 2):
            s[lo + i], s[hi - i] = s[hi - i], s[lo + i]

    reverse_all()
    last_index = len(s) - 1
    i, last_word_index = 0, 0
    while i <= last_index:
        if s[i] == " ":
            reverse_one(last_word_index, i - 1)
            i += 1
            last_word_index = i
        else:
            i += 1

    # Reverse last
    reverse_one(last_word_index, last_index)
