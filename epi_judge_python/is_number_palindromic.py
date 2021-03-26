from test_framework import generic_test

import math

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    
    digits = math.floor(math.log10(x)) + 1
    mask = pow(10, digits - 1)

    for i in range(digits // 2):
        front = x // mask
        back = x % 10
        if front != back:
            return False

        # remove from front
        x %= mask

        # remove lsd
        x = x // 10

        # reduce mask by 2 digits
        mask = mask // 100

    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
