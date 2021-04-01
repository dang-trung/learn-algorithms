def recursive_factorial(number):
    if number == 0:
        return 1
    else:
        return recursive_factorial(number - 1) * number

    