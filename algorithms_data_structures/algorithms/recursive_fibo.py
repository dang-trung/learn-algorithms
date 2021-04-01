def recursive_fibo(pos):
    if pos <= 1:
        return pos
    else:
        return recursive_fibo(pos - 1) + recursive_fibo(pos - 2)


import numpy as np


def recursive_fibo_efficient(pos):
    """
    memorization for efficiency
    with memorization, it is faster, with maximum possible pos as 46
    first function can't do this

    """

    fibo = np.arange(0, pos + 1, 1)
    for pos in range(2, pos + 1):
        fibo[pos] = fibo[pos - 1] + fibo[pos - 2]
    return fibo[pos]
