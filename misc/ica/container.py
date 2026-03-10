class IntegerContainer:
    def __init__(self):
        self.container = {} # # key: value, value: count
        self.total = 0      # Total number of integers

    def add(self, value: int) -> int:
        """
        Should add the specified integer `value` to the container
        and return the number of integers in the container after the
        addition.
        """
        if value in self.container:
            self.container[value] += 1
        else:
            self.container[value] = 1
        self.total += 1
        return self.total

    def delete(self, value: int) -> bool:
        """
        Should attempt to remove the specified integer `value` from
        the container. If the `value` is present in the container, remove it and
        return `True`, otherwise, return `False`.
        """
        if value in self.container:
            self.container[value] -= 1
            self.total -= 1
            if self.container[value] == 0:
                self.container.pop(value)
            return True
        return False

    def get_median(self) -> int | None:
        """
        Should return the median integer - the integer in the middle
        of the sequence after all integers stored in the container
        are sorted in ascending order.
        If the length of the sequence is even, the leftmost integer
        from the two middle integers should be returned.
        If the container is empty, this method should return `None`.
        """
        if not len(self.container):
            return None

        # rebuild the sorted sequence including duplicates
        arr = []
        for value, count in self.container.items():
            arr.extend([value] * count)

        arr.sort()
        size = len(arr)

        if size % 2 == 1:
            return arr[size // 2]
        else:
            return arr[size // 2 - 1]
