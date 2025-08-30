"""Crawler playground.

 u1
 u2,   u3
     u5   u6
        u1   u7
"""

import collections

RenderResult = collections.namedtuple("RenderResult", ('title', 'children'))
URLS = {
    'u1': ['u2', 'u3'],
    'u2': [],
    'u3': ['u5', 'u6'],
    'u5': [],
    'u6': ['u1', 'u7'],
    'u7': []
}


def render (url):
    return URLS[url]


def crawl(url):
    marked = set()
    queue = collections.deque()
    queue.append(url)

    while queue:
        v = queue.popleft()
        for w in render(v):
            if w not in marked:
                marked.add(w)
                queue.append(w)

    return marked

