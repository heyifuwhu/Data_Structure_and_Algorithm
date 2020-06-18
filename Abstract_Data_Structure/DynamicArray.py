import ctypes


class DynamicArray(object):
    def _init__(self):
        self._n = 0
        self.capacity = 1
        self._A = self._make_array(self.capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if 0 <= k < self.n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self.capacity)
        self._A[self._n] = obj
        self._n += 1

    def resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self.capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

if __name__ == "__main__":
    pass