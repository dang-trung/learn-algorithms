# O(2^n)
def bad_fibonacci(n):
    if n <= 1:
        print(n)
        return n
    else:
        print(n)
        return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)

# O(n)
def good_fibonacci(n):
    if n <= 1:
        print(n)
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        print(n)
        return (a + b, a)

if __name__ == '__main__':
    x = bad_fibonacci(10)
    print('----------')
    y = good_fibonacci(10)
    print('----------')
    print(x, y)
