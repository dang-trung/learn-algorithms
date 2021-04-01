def swap(array, first_index, second_index):
    origin_second = array[second_index]
    array[second_index] = array[first_index]
    array[first_index] = origin_second


if __name__ == '__main__':
    array = [1, 5, 3, 2, 6]
    swap(array, 1, 3)
    print(array)
