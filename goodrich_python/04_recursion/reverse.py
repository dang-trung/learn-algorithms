def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


def reverse_iterative(S, start, stop):
    start, stop = 0, len(S)
    while start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        start += 1
        stop -= 1


if __name__ == '__main__':
    S = [1, 4, 3, 2]
    reverse(S, 0, 4)
    print(S)
    S = [1, 4, 3, 2]
    reverse_iterative(S, 0, 4)
    print(S)