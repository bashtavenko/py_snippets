"""12.6 Find the nearest repeated entries in array.


Find the distance between the closest pair of equal entries.
'All work and no play makes for no work no fun and no results'

2nd and 3rd occurrence of 'no'
"""


def find_nearest_repetition(text):
    # Need to keep track the last occurrence of each word
    # {'All': 0, 'work': 1, 'and': 2, 'no': 3 ...}
    word_latest_index, current_min = {}, float("inf")

    for i, word in enumerate(text):
        if word in word_latest_index:
            word_index = word_latest_index[word]
            current_min = min(current_min, i - word_index)
        word_latest_index[word] = i

    return current_min


if __name__ == "__main__":
    print(
        find_nearest_repetition(
            "All work and no play makes for no work no fun and no results".split(" ")
        )
    )
