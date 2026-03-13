"""Credit to https://github.com/EricZheng0404/LibreSignal/tree/main/Questions/storage"""


class Storage:
    def __init__(self):
        self.db = {}  # { name: size }

    def add_file(self, name, size):
        if name not in self.db:
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
