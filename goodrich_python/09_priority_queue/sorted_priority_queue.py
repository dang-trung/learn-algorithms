from .priority_queue_base import PriorityQueueBase
from ..linked_list.positional_doubly_linked import PositionalList


class SortedPriorityQueue(PriorityQueueBase):  # base class defines _Item
    """Priority Queue implemented with a Sorted List, where the first element
    has the minimum key."""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def min(self):
        """Return the key-value tuple of the element with the minimum key."""
        if self.is_empty():
            raise Empty('Priority Queue is empty.')
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        """Remove and then return key-value tuple of element with min key."""
        if self.is_empty():
            raise Empty('Priority Queue is empty.')
        p = self._data.first()
        item = self._data.delete(p)
        return item._key, item._value

    def add(self, key, value):
        """Add a key-value pair to the Priority Queue."""
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(walk)
        else:
            self._data.add_before(walk, newest)

class Empty(Exception):
    pass
