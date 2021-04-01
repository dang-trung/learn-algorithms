def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        cur = A[i]
        p = i
        while p > 0 and A[p-1] > cur:
            A[p] = A[p-1]
            p -= 1
        A[p] = cur

if __name__ == '__main__':
    A = [3, 2, 5, 4]
    print(f'Before sorted: {A}[[')
    insertion_sort(A)
    print(f'After sorted: {A}')