from swap import swap


def find_min_index(array, start_index):
    min_index = start_index
    for i in range(start_index, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index


def sort_selection(array):
    for i in range(len(array)):
        swap(array, i, find_min_index(array, i))


if __name__ == '__main__':
    array = [5, 4, 2, 3, 1, 6]
    sort_selection(array)
    print(array)
