class CircularQueue:
    class _Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._tail.next

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        old_head = self._tail.next
        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = old_head.next
        self._size -= 1
        return old_head.element

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self._tail.next
        self._tail = new_node
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail.next

class Empty(Exception):
    pass
