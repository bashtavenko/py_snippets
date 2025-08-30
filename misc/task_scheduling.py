"""Task scheduling.

There are several types of tasks - 1, 2, 3, 4. Tasks have to sequenced so that
there is at least k space in between. For example, given [1, 1, 2] and k = 1,
the optimum task scheduling sequence is 1, 2, 1.  Sequence of 2, 1, None, 1 is
also possible, but it's not optimal.

Return optimal sequence.
"""


class TaskEntry:
    def __init__(self, occurences_left, last_index):
        self.occurences_left = occurences_left
        self.last_index = last_index


def get_sequence(data, k):
    """
    1. Group tasks by number of occurrences
    2. Put them into max priority queue (task with the highest occrence first)
    3. Pop all tasks from the priority queue and add to output. While poping
       store occurrences left and last index the task went to. Put the tasks into
       queue.
    4. Peek into queue head and if task is ready to go, pop it, reduce the number of
       occurrences and put it back to queue. If not ready keep adding empty runs.
    """
