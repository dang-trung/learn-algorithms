class Range:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise ValueError()

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step


if __name__ == '__main__':
    r = range(8, 140, 5)
    R = Range(8, 140, 5)

    print(f"{len(r)} {len(R)}")
    print(f"{r[15]} {R[15]}")
