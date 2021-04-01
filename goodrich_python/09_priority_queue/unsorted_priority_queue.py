from .priority_queue_base import PriorityQueueBase
from ..linked_list.positional_doubly_linked import PositionalList


class UnsortedPriortyQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def _find_min(self):
        """Return Position of the item with minimum key."""
        if self.is_empty():
            raise Empty('Priority Queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if small.element() < walk.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        """Return the item with minimum key."""
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value


class Empty(Exception):
    pass
