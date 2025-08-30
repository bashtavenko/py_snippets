"""Majority element.

More than half the strings are repetitions of single string
"bacaaabaac" a => 6 times
a: 6, b:2, c:2. length: 10

The key is 'more than half', that is
"bbbbcaa" => b
b:4, a:2, c:1. Length: 7

Boyer-Moore method:
Count 'b' and then if it's not 'b', decrease count.
Works like magic. Good for streaming.

Also, we can do randomized sampling.
Brute force is a hash table, but it would require O(N) space
"""


def majority_search(input_stream):
    candidate, candidate_count = None, 0
    for it in input_stream:
        if candidate_count==0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate==it:
            candidate_count += 1
        else:
            candidate_count -= 1
    return candidate
