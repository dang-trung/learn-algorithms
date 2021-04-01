class _DoublyLinkedBase:
    class _Node:
        __slots__ = 'element', 'prev', 'next'

        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._link_nodes(self._header, self._trailer)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, None, None)
        self._link_nodes(predecessor, new_node)
        self._link_nodes(new_node, successor)
        self._size += 1
        return new_node

    def _delete_node(self, node):
        predecessor = node.prev
        successor = node.next
        self._link_nodes(predecessor, successor)
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None  # Garbage collection
        return element

    def _link_nodes(self, predecessor, successor):
        predecessor.next = successor
        successor.prev = predecessor
