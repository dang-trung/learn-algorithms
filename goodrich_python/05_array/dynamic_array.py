import ctypes


class DynamicArray:
    """
    Array that automatically increases its capacity to add new elements (as
    soon as the current capacity ran out)
    """
    def __init__(self):
        """Create an empty array"""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()


if __name__ == '__main__':
    array = DynamicArray()
    array.append(1)
    print(len(array))  # 1
    array.append(3)
    print(array[1])  # 3
    array.append(2)
    print(len(array))  # 3
    array.append(5)
    print(array[3])  # 5
