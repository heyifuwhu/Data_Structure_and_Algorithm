from Abstract_Data_Structure.empty import Empty

class ArrayQueue(object):
    """
    FIFO queue implementation using a Python list as underlying storage.
    """
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty.")
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise  Empty("Queue is empty.")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size = -1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self.data[avail] = e
        self._size +=1

    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        walk = self._front
        for i in range(self._size):
            self._data[i] == old[walk]
            walk = (1+walk) % len(old)
        self._front = 0