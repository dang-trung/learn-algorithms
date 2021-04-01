def max_recursive(S):
    n = len(S)
    if n == 1:
        return S[-1]
    else:
        return max(S[-1], max_recursive(S[:-1]))

if __name__ == '__main__':
    S = [1, 4, 3, -5, -4, 8, 6]
    print(max_recursive(S))