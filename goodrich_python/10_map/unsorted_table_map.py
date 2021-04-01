from .map_base import MapBase


class UnsortedTableMap(MapBase):
    """
    An implementation of Map using Unsorted List.
    O(n) for basic map operations (get, set, del items).
    """

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError(f'KeyError: Key {k} does not exist.')

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        raise KeyError(f'KeyError: Key {k} does not exist.')

    def __delitem__(self, k):
        for i in range(len(self._table)):
            item = self._table[i]
            if item._key == k:
                self._table.pop(i)
                return
        raise KeyError(f'KeyError: Key {k} does not exist.')

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key
