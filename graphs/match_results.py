"""Match results.
Given a list of outcomes of matches between pairs of team, is there a sequence
of teams starting with a and ending with b such that each team in the sequence
has beaten the next team in the sequence?

a -> b
b -> c
c -> d
So basically, is there a path between two vertices in digraph?
Run dfs from v and check if w is marked.
"""

import collections

MatchResult = collections.namedtuple("MatchResult", ("winning_team", "losing_team"))


def can_team_a_beat_team_b(results, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in results:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr==dest:
            return True
        elif curr in visited or curr not in graph:
            return False
        visited.add(curr)
        return any(is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)


def can_team_a_beat_team_b_v2(results, team_a, team_b):
    def run_dfs(v):
        marked.add(v)
        for w in graph[v]:
            if w not in marked:
                run_dfs(w)

    graph = collections.defaultdict(set)
    for result in results:
        graph[result.winning_team].add(result.losing_team)
    marked = set()
    run_dfs(team_a)
    return team_b in marked
