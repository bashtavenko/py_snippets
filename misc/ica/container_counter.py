from collections import Counter

class Container:
    def __init__(self):
        self.counter = Counter()

    def add(self, value: int) -> int:
        self.counter[value] += 1
        return sum(self.counter.values())

    def delete(self, value: int) -> bool:
        if self.counter[value] > 0:
            self.counter[value] -= 1
            if self.counter[value] == 0:
                del self.counter[value]
            return True
        return False