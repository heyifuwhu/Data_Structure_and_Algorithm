import ctypes


class DynamicArray(object):
    """A dynamic array class akin to a simplified Python list"""

    def __init__(self):
        """Create an empty array"""
        self._capacity = 1
        self._n = 0
        self._A = self._make_array(self._capacity)

    def show(self):
        print(self._A[:self._n])

    def append(self, obj):
        """Add element to end of the array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, v):
        """Insert value at index k, shifting subsequent values rightward"""
        # assume 0 <= k <= n
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i-1]
        self._A[k] = v
        self._n += 1

    def pop(self, k):
        pass

    def extend(self, arr):
        pass

    def remove(self, value):
        """Remove first occurrence of value()or raise ValueError"""
        # note: we don't consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n-1] = None
                self._n -= 1
                return
        raise ValueError('value not found')

    def _resize(self, c):
        """Resize internal array to capacity c"""
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """low-level array"""
        return (c * ctypes.py_object)()

    def __len__(self):
        """Return number of elements stored in the array"""
        return self._n
    #
    # def __str__(self):
    #     print(self._A[:self._n])
    #     # return None

    def __getitem__(self, k):
        """Return the element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def __setitem__(self, k, v):
        """Assign v to the element at index k"""
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        self._A[k] = v


if __name__ == "__main__":
    arr = DynamicArray()
    for i in range(5):
        arr.append(i)
    arr.show()
    arr[0] = 10
    arr.show()
    arr.remove(10)
    arr.show()
    try:
        arr.remove(10)
    except Exception as e:
        print(e)

    arr.insert(0, 15)
    arr.show()

    # Python List Class
    # from time import time
    # def compute_average(n):
    #     data = []
    #     start = time()
    #     for k in range(n):
    #         data.append(k)
    #     end = time()
    #     return (end-start)/n
    #
    # for i in range(2, 9):
    #     num = 10**i
    #     print(num, compute_average(num))
