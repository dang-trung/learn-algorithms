def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S1, S2, S)

if __name__ == '__main__':
    arr = [3, 9, 2, 1, 5, 10, 3]
    merge_sort(arr)
    print(arr)