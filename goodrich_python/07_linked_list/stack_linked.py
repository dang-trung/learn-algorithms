class LinkedStack:
    class _Node:
        __slots__ = 'element', 'next'

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        output = self._head.element
        self._head = self._head.next
        self.size -= 1
        return output

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head.element


class Empty(Exception):
    pass
