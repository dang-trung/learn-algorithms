def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


def fast_power(x, n):
    if n == 0:
        return 1
    else:
        partial = fast_power(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


if __name__ == '__main__':
    print(power(3, 4) - 3 ** 4)
    print(fast_power(3, 4) - 3 ** 4)
    print(fast_power(2, 5) - 2 ** 5)

