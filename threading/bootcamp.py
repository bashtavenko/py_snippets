"""Threading."""
import threading


"""
Also: threading.Lock()

lock = threading.Lock()

with MyClass.lock:
   # Foo
   
"""

class Semaphore():

    def __init__(self, max_available):
        self.cv = threading.Condition()
        self.MAX_AVAILABLE = max_available
        self.taken = 0 # Access is guarded

    def acquire(self):
        self.cv.acquire()
        while (self.taken == self.MAX_AVAILABLE):
            self.cv.wait()  # Blocks until notify()
        self.taken += 1     # Only one thread can enter
        self.cv.release()

    def release(self):
        self.cv.acquire()
        self.taken -= 1
        self.cv.notify()
        self.cv.release()
