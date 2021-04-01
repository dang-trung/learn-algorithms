import unittest


def factorial(n):
    """
    A function to compute factorial of a n number.

    Parameters
    ----------
    n : int
        input number

    Returns
    -------
    int
        output number

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(30)
    265252859812191058636308480000000
    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    RecursionError: maximum recursion depth exceeded in comparison
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

class MyTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
    
    def test_factorial_second(self):
        self.assertEqual(factorial(2), 2)

    def test_Factorial_third(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_fail(self):
        self.assertRaises(RecursionError, factorial, 30.1)
    
    def test_factorial_fail_second(self):
        self.assertRaises(TypeError, factorial, "abc")

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    unittest.main()

