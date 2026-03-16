"""Credit to https://github.com/EricZheng0404/LibreSignal/tree/main/Questions/storage"""
import pathlib

class Storage:
    def __init__(self):
        self.db = {}  # { name: size }

    def add_file(self, name, size):
        if name in self.db:
            return False

        self.db[name] = size
        return True

    def get_file_size(self, name):
        if name not in self.db:
            return ""
        return self.db[name]

    def delete_file(self, name):
        if name not in self.db:
            return ""
        size = self.db[name]
        self.db.pop(name)
        return size

    def query(self, prefix, suffix):
        result = []
        for full_path, size in self.db.items():
            p = pathlib.Path(full_path)
            top_dir = p.parts[1] if len(p.parts) > 1 else ""
            basename = p.name
            file_size = size
            if prefix == top_dir and suffix == basename:
                result.append((full_path, file_size))
        # We have (path, size) tuples
        # The key should be (-size, path)
        # -size makes the sort descending
        # path keeps alphabetical order when sizes are equal
        result.sort(key=lambda x: (-x[1], x[0]))
        return [f"{path}({size})" for path, size in result]
