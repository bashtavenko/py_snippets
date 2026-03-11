"""Basic integer container with one step."""


class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """

    def __init__(self):
        self.container = {}  # value:count

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        self.container[value] = self.container.get(value, 0) + 1

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        if value not in self.container:
            return False
        else:
            self.container[value] -= 1
            if self.container[value] == 0:
                self.container.pop(value)
            return True

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """

        if not len(self.container):
            raise ValueError("Empty array")

        arr = []
        for value, count in self.container.items():
            arr.extend([value] * count)
        arr.sort()
        size = len(arr)
        if size % 2 == 1:
            return arr[size // 2]  # even
        else:
            return arr[size // 2 - 1]  # odd, leftmost integer