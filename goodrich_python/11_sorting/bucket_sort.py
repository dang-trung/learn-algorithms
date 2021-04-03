def insertion_sort(bucket):
    n = len(bucket)
    for i in range(1, n):
        while i > 0 and bucket[i] < bucket[i-1]:
            bucket[i], bucket[i-1] = bucket[i-1], bucket[i]
            i -= 1


def bucket_sort_float_under_one(arr):
    buckets = [[] for i in range(10)]
    for ele in arr:
        key = int(10 * ele)
        buckets[key].append(ele)

    for bucket in buckets:
        insertion_sort(bucket)

    i = 0
    for bucket in buckets:
        for ele in bucket:
            arr[i] = ele
            i += 1


def bucket_sort(arr, num_bucket=5):
    max_ele = max(arr)
    min_ele = min(arr)

    dist = (max_ele - min_ele) / num_bucket
    buckets = [[] for i in range(num_bucket)]
    for ele in arr:
        key = int((ele - min_ele) / dist)
        if ele == max_ele:
            key -= 1
        buckets[key].append(ele)
    
    for bucket in buckets:
        insertion_sort(bucket)
    
    i = 0
    for bucket in buckets:
        for ele in bucket:
            arr[i] = ele
            i += 1

if __name__ == '__main__':
    bucket = [2, 5, 1, 2, 6, 3]
    insertion_sort(bucket)
    print(bucket)
    print('-' * 40)

    floats_under_one = [0.897, 0.565, 0.656,
                        0.1234, 0.665, 0.3434]
    bucket_sort_float_under_one(floats_under_one)
    print(floats_under_one)
    print('-' * 40)
    
    floats = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
    bucket_sort(floats)
    print(floats)
    print('-' * 40)
