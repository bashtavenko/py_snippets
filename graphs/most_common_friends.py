"""Find a user with most common friends.

1 - 8 - 7
  - 2 - 4
  - 3 - 4 - 5


Adjacency lists:
1: 8, 2, 3
8: 1, 7
7: 8
2: 1, 4
3: 1, 4
4: 2, 3, 5
"""

import collections
import operator

"""Version with adjacency list."""


class Network:
    def __init__(self):
        self.graph = collections.defaultdict(set)

    def add_user(self, v, w):
        self.graph[v].add(w)
        self.graph[w].add(v)

    def find_user(self, s):
        # Inverted set where key is target vertex and value is number of common friends
        friends = collections.defaultdict(int)
        for v in self.graph[s]:  # Check only friends of s
            # See how many other nodes have 'v' as friend
            for w in self.graph[v]:
                if w!=s:
                    friends[w] += 1

        # Return key with the highest count:
        # {7: 1, 4: 2}, returns 4
        return max(friends.items(), key=operator.itemgetter(1))[0]


"""Version with friends at the Node."""


class Person:
    def __init__(self, v, friends):
        self.v = v
        self.friends = friends


class Network2:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        self.people[person.v] = person.friends

    def find_user(self, s):
        # Inverted set where key is target vertex and value is number of common friends
        friends = collections.defaultdict(int)

        for v in self.people[s]:
            for w in self.people[v]:
                if w!=s:
                    friends[w] += 1

        # Return key with the highest count:
        # {7: 1, 4: 2}, returns 4
        return max(friends.items(), key=operator.itemgetter(1))[0]
