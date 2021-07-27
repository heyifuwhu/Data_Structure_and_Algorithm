class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

class LinkedList(object):
    """
    -- Double Linked List --
    append: O(1)
    pop: O(1)
    __getitem__, __setitem__: O(1)

    """

    def __init__(self, L=None):
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.hashmap = dict()

        if isinstance(L, type(None)):
            self.head.next, self.tail.prev = self.tail, self.head
        elif isinstance(L, list):
            self.size = len(L)
            cursor = self.head
            for i in range(len(L)):
                node = Node(L[i])
                self.hashmap[i] = node
                cursor.next, node.prev = node, cursor
                cursor = cursor.next
            self.tail.prev, cursor.next = cursor, self.tail
            # self.show()

    def _is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def append(self, val):
        node = Node(val)
        self.hashmap[self.size] = node
        self.size += 1
        self.tail.prev.next, node.prev = node, self.tail.prev
        self.tail.prev, node.next = node, self.tail
        # self.show()

    def pop(self):
        if not self._is_empty():
            self.size -= 1
            # remove the value at tail
            value = self.hashmap[self.size].val
            self.hashmap[self.size-1].next = None
            del self.hashmap[self.size]
            # self.show()
            return value
        else:
            raise IndexError('pop from empty list')

    def show(self):
        cursor = self.head
        for i in range(self.size):
            cursor = cursor.next
            print(cursor.val, end=' ')
        print()

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        if idx < self.size:
            return self.hashmap[idx].val
        else:
            raise IndexError('list index out of range')

    def __setitem__(self, idx, value):
        if idx < self.size:
            self.hashmap[idx].val = value
        else:
            raise IndexError('list index out of range')


if __name__ == '__main__':
    obj1 = LinkedList()
    obj2 = LinkedList(L=[1, 3, 5])
    for i in range(1, 6):
        obj1.append(i)
        obj2.append(i)
    obj1.show()
    obj2.show()





