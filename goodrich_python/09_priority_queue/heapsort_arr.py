class Solution:
    def parent(self, arr, i):
        return (i-1) // 2

    def left_child(self, arr, i):
        return 2 * i + 1

    def right_child(self, arr, i):
        return 2 * i + 2

    def has_left_child(self, arr, n, i):
        return self.left_child(arr, i) < n

    def has_right_child(self, arr, n, i):
        return self.right_child(arr, i) < n

    def downheap(self, arr, n, i):
        if self.has_left_child(arr, n, i):
            left = self.left_child(arr, i)
            large_child = left
            if self.has_right_child(arr, n, i):
                right = self.right_child(arr, i)
                if arr[right] > arr[left]:
                    large_child = right

            if arr[large_child] > arr[i]:
                arr[large_child], arr[i] = arr[i], arr[large_child]
                self.downheap(arr, n, large_child)

    def heapify(self, arr, n):
        start = self.parent(arr, n - 1)
        for index in range(start, -1, -1):
            self.downheap(arr, n, index)

    def HeapSort(self, arr, n):
        self.heapify(arr, n)
        arr[0], arr[-1] = arr[-1], arr[0]
        for k in range(n - 1, -1, -1):
            # print(arr)
            arr[0], arr[k] = arr[k], arr[0]
            self.heapify(arr, k)

if __name__ == "__main__":
    arr = [4, 1, 3, 3, 9, 7]
    n = 5
    test = Solution()
    test.HeapSort(arr=arr, n=n)
    # test.heapify(arr, n)
    print(arr)