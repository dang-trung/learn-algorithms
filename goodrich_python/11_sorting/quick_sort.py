def quick_sort(arr):
    # Could be more memory efficient if implemented with Queue instead of Array
    # Could be even more efficient if implemented inplace with Array (next function)
    n = len(arr)
    if n < 2:
        return arr
    pivot = arr[-1]
    less, equal, greater = [], [pivot], []
    for ele in arr[:-1]:
        if ele < pivot:
            less.append(ele)
        elif ele > pivot:
            greater.append(ele)
        else:
            equal.append(ele)

    less = quick_sort(less)
    greater = quick_sort(greater)

    arr = []
    for part in [less, equal, greater]:
        if part is not None and len(part) > 0:
            for ele in part:
                arr.append(ele)
    return arr

def quick_sort_inplace(arr, a, b):
    if a >= b:
        return
    pivot = arr[b]
    l = a
    r = b - 1
    while l <= r:
        if arr[l] <= pivot:
            l += 1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            r -= 1
    arr[l], arr[b] = arr[b], arr[l]
    quick_sort_inplace(arr, a, l-1)
    quick_sort_inplace(arr, l+1, b) 

if __name__ == '__main__':
    arr = [3, 9, 2, 1, 5, 10, 3]
    print(f'Before: {arr}')
    arr = quick_sort(arr)
    print(f'After: {arr}')

    arr2 = [3, 9, 2, 1, 5, 10, 3, 2, 3, 6, 10, 15, 12, 1, 2, 4]
    print(f'Before: {arr2}')
    quick_sort_inplace(arr2, 0, len(arr2) - 1)
    print(f'After: {arr2}')
