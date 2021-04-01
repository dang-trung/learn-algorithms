def search_binary(input_array, value):
    left, right = 0, (len(input_array) - 1)
    while True:
        if left <= right:
            mid = int((left + right)/2)
            if input_array[mid] == value:
                return mid
            elif input_array[mid] < value:
                left = mid + 1
            elif input_array[mid] > value:
                right = mid - 1
        else:
            return -1

if __name__ == '__main__':
    input_array = [1, 2, 3, 4, 5, 6]
    search_binary(input_array, 3)
    search_binary(input_array, 7)