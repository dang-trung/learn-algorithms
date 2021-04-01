def partition(A, p, r):
    x = A[r]  # pivot
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:  # if value in check is smaller than pivot, swap it in the
            # positions f
            i = i + 1
            A[i], A[j] = A[j], A[i]
            # else (larger), do nothing (keep it at the original pos)
    A[i + 1], A[r] = A[r], A[i + 1]  # exchange the pivot with the first element of larger partition
    return i + 1  # return the pivot index


def sort_quick(A, p, r):
    if p < r:
        q = partition(A, p, r)  # keep divide the
        sort_quick(A, p, q - 1)
        sort_quick(A, q + 1, r)
