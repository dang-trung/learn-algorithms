from .priority_queue_base import PriorityQueueBase


class HeapPriorityQueue(
    PriorityQueueBase):  # base class defines _Item and is_empty() method
    """
    Heap-based implementation for Priority Queue.
    Data stored in a Python list.
    """

    def __init__(self, content=()):
        self._data = [self._Item(key, value) for key, value in content]
        if len(self._data) > 1:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def __len__(self):
        return len(self._data)

    def _parent(self, j):
        """Return the index of node j's parent."""
        return (j - 1) // 2

    def _right(self, j):
        """Return the index of node j's right child."""
        return 2 * j + 1

    def _left(self, j):
        """Return the index of node j's left child."""
        return 2 * j + 2

    def _has_right(self, j):
        return self._right(j) < len(self)

    def _has_left(self, j):
        return self._left(j) < len(self)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        """Swap the node at j up to the position that satisfies min heap
        order."""
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def add(self, key, value):
        """Add an item containing key-value to the priority queue."""
        self._data.append(self._Item(key, value))
        self._upheap(len(self) - 1)

    def _downheap(self, j):
        """Swap the node at j down to the position that satisfies min heap
        order."""
        if self._has_left(j):
            left = self._left(j)
            child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[child]:
                    child = right
            if self._data[child] < self._data[j]:
                self._swap(child, j)
                self._downheap(child)

    def min(self):
        """Return the key-value of the item with minimum key"""
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority queue is empty.')
        self._swap(0, len(self) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value


class Empty(Exception):
    pass
