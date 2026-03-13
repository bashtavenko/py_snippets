"""Credit to https://github.com/EricZheng0404/LibreSignal/blob/main/Questions/in_memory_database/test_in_memory_database.py"""


class InMemoryDatabase:
    def __init__(self):
        self.db = {}  # {key : {field: (value, expire_at)}}
        # Expire_at is None if no TTL

    # ========== Level 1 Operations ==========
    def set(self, key, field, value):
        if key in self.db:
            self.db[key][field] = value
        else:
            self.db[key] = {field: value}
        return ""

    def get(self, key, field):
        if key not in self.db or field not in self.db[key]:
            return ""
        return self.db[key][field]

    def delete(self, key, field):
        if key not in self.db or field not in self.db[key]:
            return "false"
        self.db[key].pop(field)
        return "true"

    # ========== Level 2 Operations ==========
    def scan(self, key):
        if key not in self.db:
            return ""

        # # Sort a result lexicographically
        result_list = [f"{field}({value})" for field, value in sorted(self.db[key].items())]

        # One-liner with generator expression
        #     return ", ".join(
        #         f"{field}({value})"
        #         for field, value in sorted(self.db[key].items())
        #     )
        return ", ".join(result_list)

    def scan_by_prefix(self, key, prefix):
        if key not in self.db:
            return ""

        # ... or this could be compacted
        result_list = []
        for field, value in sorted(self.db[key].items()):
            if field.startswith(prefix):
                result_list.append(f"{field}({value})")
        return ", ".join(result_list)

    # ========== Level 3 Operations ==========
    def set_at(self, key, field, value, timestamp):
        # Ignore timestamp
        if key in self.db:
            self.db[key][field] = (value, None)
        else:
            self.db[key] = {field: (value, None)}
        return ""

    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        # This is where we store absolute expiration
        if key in self.db:
            self.db[key][field] = (value, timestamp + ttl)
        else:
            self.db[key] = {field: (value, timestamp + ttl)}
        return ""

    def delete_at(self, key, field, timestamp):
        pass

    def get_at(self, key, field, timestamp):
        if key not in self.db or field not in self.db[key]:
            return ""

        value, expire_at = self.db[key][field]
        if expire_at is not None and timestamp >= expire_at:
            return ""

        return value

    def scan_at(self, key, timestamp):
        pass

    def scan_by_prefix_at(self, key, prefix, timestamp):
        pass
