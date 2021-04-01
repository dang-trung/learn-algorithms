from goodrich_python.linked_list.doubly_linked import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """Return position s node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a Position instance')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node.next is None:
            raise ValueError('p has been deleted from the list')
        return p._node

    def _make_position(self, node):
        """Return Position instance for a non-sentinel node"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header.next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer.prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is
        first)"""
        node_p = self._validate(p)
        return self._make_position(node_p.prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is
        last)"""
        node_p = self._validate(p)
        return self._make_position(node_p.next)

    def __iter__(self):
        """Make the list iterable (i.e. support for loops)"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # override inherited mutators to return Position rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header.next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer.prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new
        Position."""
        original = self._validate(p)
        return self._insert_between(e, original.prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new
        Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original.next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original.element  # temporarily store old element
        original.element = e  # replace with new element
        return old_value  # return the old element value

if __name__ == '__main__':
    L = PositionalList()
    print(L.add_last(8).element())