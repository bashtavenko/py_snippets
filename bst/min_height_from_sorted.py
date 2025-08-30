""" 14.9 Build a minimum height BST from a sorted array

 Common sense - take medium recursively .
"""

import bootcamp


def build_min(data):
    def run(start, end):
        if start >= end:
            return None

        mid = (start + end) // 2
        return bootcamp.BSTNode(
            data[mid], left=run(start, mid), right=run(mid + 1, end)
        )

    return run(0, len(data))


if __name__=="__main__":
    sorted_list = [8, 10, 12, 20, 25, 30, 40]
    print(build_min(sorted_list))
