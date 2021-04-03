def count_sort_zero_nine(arr):
    count = [0] * 10
    output = [0] * len(arr)
    for ele in arr:
        count[ele] += 1
    
    for i in range(len(count) - 1):
        count[i+1] += count[i]
    
    for ele in arr[::-1]:
        count[ele] -= 1
        output[count[ele]] = ele

    return output

def count_sort_character(str):
    count = [0] * 256
    output = [""] * len(str)

    for char in str:
        count[ord(char)] += 1

    for i in range(len(count) - 1):
        count[i+1] += count[i]

    for char in str[::-1]:
        count[ord(char)] -= 1
        output[count[ord(char)]] = char

    return "".join(output)

def count_sort_negative_int(arr):
    max_ele = max(arr)
    min_ele = min(arr)
    range_ele = max_ele - min_ele + 1
    
    count = [0] * range_ele
    output = [0] * len(arr)

    for ele in arr:
        count[ele - min_ele] += 1

    for i in range(range_ele - 1):
        count[i+1] += count[i]

    for ele in arr[::-1]:
        count[ele - min_ele] -= 1
        output[count[ele - min_ele]] = ele

    return output

if __name__ == "__main__":
    arr = [1, 4, 1, 2, 7, 5, 2]
    arr = count_sort_zero_nine(arr)
    print(arr)

    str = 'geeksforgeeks'
    str = count_sort_character(str)
    print(str)

    arr2 = [-5, -10, 0, -3, 8, 5, -1, 10]
    arr2 = count_sort_negative_int(arr2)
    print(arr2)
