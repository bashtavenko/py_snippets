import collections
import heapq


def set_callback(cb):
    pass


def set_timeout(relative_ms):
    2


def get_time():
    42


def add_callback(cb, ms):
    Event = collections.namedtuple("Event", ("callback", "go_off_time"))
    min_heap = []
    heapq.heapify(min_heap)

    def internal_callback():
        ev = heapq.heappop(min_heap)
        ev.callback()

    go_off_time = ms + get_time()
    event = Event(cb, go_off_time)
    heapq.heappush(min_heap, event)
    set_callback(internal_callback)


def callback_1():
    print("cb1")


def callback_2():
    print("cb1")


if __name__=="__main__":
    add_callback(callback_1, 200)
    add_callback(callback_2, 400)
