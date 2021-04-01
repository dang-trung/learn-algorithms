def is_palindrome(string):
    """recursion solution"""
    string = string.lower()
    if len(string) <= 1:
        print("A palindrome!")
        return True
    else:
        if string[0] == string[-1]:
            is_palindrome(string[1: len(string) - 1])
        else:
            print("Not a palindrome!")


if __name__ == '__main__':
    is_palindrome('tenet')
    is_palindrome('dog')
