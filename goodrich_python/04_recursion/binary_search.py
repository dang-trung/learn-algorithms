def binary_search(data, target, low, high):
    # assume data is sorted
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)

def iter_binary_search(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == '__main__':
    array = [1, 2, 4, 5, 7, 9]
    print(binary_search(array, 2, 0, 5))
    print(iter_binary_search(array, 2, 0, 5))
    print(binary_search(array, 10, 0, 5))
    print(iter_binary_search(array, 10, 0, 5))
