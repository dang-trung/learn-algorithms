class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise EmptyStack('Empty stack')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise EmptyStack('Empty stack')
        return self._data[-1]


class EmptyStack(Exception):
    pass


def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


if __name__ == '__main__':
    print(is_matched('()[]{([])}'))  # True
    print(is_matched('()[]{([]}'))  # FalseD
