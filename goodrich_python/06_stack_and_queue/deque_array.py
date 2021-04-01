class Deque:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._front = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def first(self):
        return self._data[self._front]

    def last(self):
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        avail = (self._front - 1) % len(self._data)
        self._data[avail] = e
        self._front = avail
        self._size += 1

    def add_last(self, e):
        if self._size == len(self._data):
            self._resize(len(self._data) * 2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        output = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) / 4:
            self._resize(len(self._data) // 2)
        return output

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty.')
        back = (self._front + self._size - 1) % len(self._data)
        output = self._data[back]
        self._data[back] = None
        self._size -= 1
        if 0 < self._size < len(self._data) / 4:
            self._resize(len(self._data) // 2)
        return output


class Empty(Exception):
    pass


if __name__ == '__main__':
    D = Deque()
    D.add_last(5)
    D.add_first(3)
    D.add_first(7)
    print(D.first())
    print(D.delete_last())
    print(len(D))
    print(D.delete_last())
    print(D.delete_last())
    D.add_first(6)
    print(D.last())
    D.add_first(8)
    print(D.is_empty())
    print(D.last())
