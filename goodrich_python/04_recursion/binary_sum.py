def binary_sum(S, start, stop):
    """
    Return sum of slice S[start:stop]
    """
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(S, start, mid) + binary_sum(S, mid, stop)

if __name__ == '__main__':
    A = [4, 2, 3, 2]
    print(binary_sum(A, 0, len(A)) - sum(A))