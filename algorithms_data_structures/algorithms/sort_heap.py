def max_heapify(A, i,
                n):  # push the element (not in the right pos) down the tree
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and A[l] > A[i]:
        largest = l
    if r < n and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[
            i]  # nice multiple assignment for swap
        max_heapify(A, largest, n)


def min_heapify(A, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i
    if l < n and A[l] < A[i]:
        smallest = l
    if r < n and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest, n)


def build_max_heap(A, n):  # start from the right-above-lowest level, keep push
    # the element (in wrong pos) down until we got a max heap
    for i in range(int((n - 1) / 2), -1, -1):
        max_heapify(A, i, n)


def sort_heap(A):  # swap the first and last element, remove last element from
    n = len(A)  # the tree, re-build our max heap, again
    build_max_heap(A, n)
    for index in range(n - 1, 0, -1):
        A[0], A[index] = A[index], A[0]
        max_heapify(A, 0, index)
