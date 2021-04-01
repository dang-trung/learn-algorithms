def insert_index(array, old_pos, new_pos):
    if old_pos > new_pos:
        key = array[old_pos]
        for i in range(old_pos, new_pos - 1, -1):
            array[i] = array[(i - 1)]
        array[new_pos] = key


def sort_insertion(array):
    for j in range(1, array.size):
        i = j - 1
        while i >= 0:
            if array[i] > array[j]:
                i = i - 1
            else:
                break
        insert_index(array, j, i + 1)
