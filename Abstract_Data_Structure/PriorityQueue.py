class PriorityQueueBase(object):
    """
    Abstract base class for priority queue
    """

    class _item(object):
        """
        Lightweight composite to store priority queue items.
        """

        __slots__ = '_key', "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        # less than operator
        def __lt__(self, other):
            return self._key < other._key


     def is_empty(self):
        return len(self) == 0