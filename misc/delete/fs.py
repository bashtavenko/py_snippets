import collections

FILE, FOLDER = range(2)
Item = collections.namedtuple('Item', ('id', 'item_type'))


class Item:
    def __init__(self, id, item_type):
        self.id = id
        self.item_type = item_type

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(id)


class FileSystem:
    def __init__(self):
        self.graph = collections.defaultdict(set)

    def match(self, id):
        """Returns list of files."""
        v = self._find_by_id(id)
        return self.graph[v] if v else []

    def delete(self, id):
        """Deletes file or empty directory."""
        v = self._find_by_id(id)
        if not v:
            return

        if self.graph[v]:
            raise ValueError()

        del v

    def is_directory(self, id):
        """Returns true or false."""
        v = self._find_by_id(id)
        return v.item_type == FOLDER if v else False

    def add(self, v1, v2):
        self.graph[v1].add(v2)

    def is_empty(self):
        return self.graph

    def _find_by_id(self, id):
        first_vertex = self.graph.keys()[0]
        return self._dfs_search(first_vertex, id, set())

    def _dfs_search(self, v, id, marked):
        if v.id == id:
            return v
        marked.add(v)
        for w in self.graph[v]:
            if w not in marked:
                result = self._dfs_search(w, id, marked)
                if result:
                    return result
        return None

