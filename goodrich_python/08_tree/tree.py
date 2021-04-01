from .queue_linked import LinkedQueue


class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemeted by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        """Return position of the root"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return position of p's parent"""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of positions of p's children"""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """Recursively compute depth of tree O(n) worst"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height(self, p):
        """Recursively compute height of tree O(n) worst"""
        if self.is_leaf(p):
            return 0
        else:
            return 1 + self._height(self.children(p))

    def height(self, p=None):
        """Allow compute height of tree by default"""
        if p is None:
            p = self.root()
        return self._height(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """Root -> Child Traversal"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p
        for child in self.children(p):
            for node in self._subtree_preorder(child):
                yield node

    def postorder(self):
        """Child -> Root Traversal"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for child in self.children(p):
            for node in self._subtree_postorder(child):
                yield node
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            Q = LinkedQueue()
            Q.enqueue(self.root())
            while not Q.is_empty():
                p = Q.dequeue()
                yield p
                for c in self.children(p):
                    Q.enqueue(c)

    def positions(self):
        return self.inorder()
