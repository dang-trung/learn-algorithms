def count_sort_zero_nine(arr):
    count = [0] * 10
    indices = [0] * len(arr)
    for ele in arr:
        count[ele] += 1

    for i in range(len(count) - 1):
        count[i+1] += count[i]

    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        indices[count[arr[i]]] = i

    return indices


def radix_sort(arr, d=3, base=10):
    n = len(arr)
    output = [0] * n
    for i in range(1, d+1):
        arr_base = [0] * n
        for j in range(n):
            try:
                arr_base[j] = int(str(arr[j])[-i])
            except IndexError:
                arr_base[j] = 0

        indices = count_sort_zero_nine(arr_base)

        for i in range(len(indices)):
            output[i] = arr[indices[i]]

        arr = output.copy()

    return output

if __name__ == '__main__':
    arr = [53, 89, 150, 36, 633, 233]
    arr = radix_sort(arr)
    print(arr)
