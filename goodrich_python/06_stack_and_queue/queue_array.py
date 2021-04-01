class ArrayQueue:
    def __init__(self, cap=10):
        self._data = [None] * cap
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]
    
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0
        
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty.')
        output = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -=1
        if 0 < self._size < len(self._data) / 4:
            self._resize(len(self._data) // 2)
        return output

class Empty(Exception):
    pass

if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(5)
    Q.enqueue(3)
    print(len(Q))
    print(Q.dequeue())
    print(Q.is_empty())
    print(Q.dequeue())
    print(Q.is_empty())
    Q.enqueue(7)
    Q.enqueue(9)
    print(Q.first())
    Q.enqueue(4)
    print(len(Q))
    print(Q.dequeue())