""" 12.5 Compute the k-most frequent queries.

"""
import collections
import heapq
import itertools


def compute_very_crude(a, k):
    # Compute frequencies very bad
    fs = {}
    for s in a:
        if s in fs:
            fs[s] += 1
        else:
           fs[s] = 1

    # Sort keys by frequencies
    sorted_keys =  sorted(fs, key=fs.get, reverse=True)
    return ['{} ({})'.format(k, fs[k]) for k in sorted_keys]


def compute_default_dict(a, k):
    fs = collections.defaultdict(int)
    for s in a:
        fs[s] += 1

    sorted_keys =  sorted(fs, key=fs.get, reverse=True)
    return ['{} ({})'.format(k, fs[k]) for k in sorted_keys]


def compute_counter(a, k):
    fs = collections.Counter(a)
    sorted_keys =  sorted(fs, key=fs.get, reverse=True)
    return ['{} ({})'.format(k, fs[k]) for k in sorted_keys]


# TODO: make it work this needs max_heap
def compute_min_heap(stream, k):
    # islice: return iterator of k elements
    fs = collections.defaultdict(int)
    for s in itertools.islice(stream, k):
        fs[s] += 1

    min_heap = [(value, item) for item, value in fs.iteritems()]
    heapq.heapify(min_heap)

    for next_string in stream:
        fs[next_string] += 1
        heapq.heappushpop(min_heap, (fs[next_string], next_string))

    return ['{} ({})'.format(s[1], s[0]) for s in min_heap]
