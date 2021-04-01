class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

if __name__ == '__main__':
    seq_ite = SequenceIterator([1, 2, 3, 4])
    print(next(seq_ite))
    print(next(seq_ite))
    print(next(seq_ite))