def is_even(number):
    if number % 2 == 0:
        return True


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


def recursive_power(base, power):
    if type(power) == int:
        if power == 0:
            return 1
        elif is_positive(power) and is_even(power):
            return recursive_power(base, int(power / 2)) ** 2
        elif is_positive(power) and not is_even(power):
            return recursive_power(base, power - 1) * base
        else:
            return 1 / recursive_power(base, - power)
    else:
        print("The power must be an interger!")


if __name__ == "__main__":
    print(recursive_power(3, 4) - 3 ** 4)
    print(recursive_power(3, -2) - 3 ** (-2))
    print(recursive_power(3, -1.5))