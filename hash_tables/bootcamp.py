""" Hashtable - space vs time.

Collision: search for a given key. Hash function leads to a "bucket" but it may
be already occupied by a DIFFERENT key (hash -> more than one key).
Separate chaining (linked list) or linear probing
(if key does not equal search key, try next entry).

Good hash function:
- should examine all characters of the string
- should give a range of values and should not let on character
  to dominate
"""

import collections


def find_anagram(dictionary):
    # Make a hashtable where key is sorted strings and values all words that
    # have the same key if sorted.
    # {'eilsv': ['elvis', 'lives', 'levis']}
    d = collections.defaultdict(list)
    for s in dictionary:
        # ''.join => convert list to string
        # Because sorted(s) returns a list
        # of characters ['e', 'i', 'l', 's', 'v'] but list is un-hashable.
        d["".join(sorted(s))].append(s)

    return [group for group in d.values() if len(group) >= 2]
