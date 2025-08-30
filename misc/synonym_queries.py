"""Synonym queries.

[(rate, ratings),
(approval, popularity)]

("obama approval rate", "obama popularity rating")  = T
("obama approval rates" ,"obama popluarity rate")   = F
("obama approval rate" ,"popularity ratings obama") = F
"""

import collections

def is_synonym(s1, s2):
    words = collections.defaultdict(set)
    words['approval'].add('popularity')
    words['popularity'].add('approval')
    words['rate'].add('rating')
    words['rating'].add('rate')

    for i, w1 in enumerate(s1):
        w2 = s2[i]
        if w1 != w2 and not w2 in words[w1]:
            return False
    return True


"""
Synonym relationships are transitive.
(score, point)
(point, grade)
(grade, result)

score point = y
score grade = y
score result = result

union-find
"""

"""
Synonyms span multiple words.
(kelly blue book, kbb)
(turn out to be, prove to be)
"""
