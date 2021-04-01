def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]

if __name__ == '__main__':
    A = [4, 2, 3, 2]
    print(linear_sum(A, len(A)) - sum(A))
