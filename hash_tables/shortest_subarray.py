""" 12.7 Find the smallest sub-array covering all values.

Input: array of strings and set of search terms (keywords).
Return the indices of the starting and ending index of a
shortest sub-array of the given array that covers the set.

Array: apple, banana, apple, apple, dog, cat, apple, dog, banana,
apple, cat, dog
Set: {banana, cat}
Answer: (8, 10)
"""

import collections


def find_smallest_subarray_covering_set(paragraph, keywords):
    keywords_to_cover = collections.Counter(keywords)
    # Counter({'banana': 1, 'cat': 1})
    result = (-1, -1)
    remaining_to_cover = len(keywords)
    left = 0
    for right, p in enumerate(paragraph):
        # 0 apple, 1 banana, 2 apple, etc.
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # print (f'right:{right} word:{p} keyword:{keywords_to_cover}')
        while remaining_to_cover==0:
            # {'banana': 0, 'cat': 0}
            print(left, right)
            if result==(-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            print(pl)
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1

    return result
