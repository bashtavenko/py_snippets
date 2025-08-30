"""Given a group of people with their birth and death years, find the years with
the highest population."""

import collections

Person = collections.namedtuple("Person", ("birth", "death"))
Bar = collections.namedtuple("Bar", ("year", "count"))


def make_histogram(people):
    """Returns histogram for the highest population."""
    counter = collections.defaultdict(int)

    # Fill counter.
    for person in people:
        for year in range(person.birth, person.death + 1):
            counter[year] += 1

    # Sort counter by count descending
    top_counts = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Return the highest
    return [Bar(item[0], item[1]) for item in top_counts[:5]]
