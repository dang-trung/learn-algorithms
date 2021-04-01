def harmonic_num(n):
    if n == 1:
        return n
    else:
        return 1/n + harmonic_num(n-1)

if __name__ == '__main__':
    print(harmonic_num(2))
    print(harmonic_num(4))