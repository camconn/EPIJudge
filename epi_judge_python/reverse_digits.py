from test_framework import generic_test

import math

def reverse(x: int) -> int:
    neg = x < 0
    result = 0
    x_rem = abs(x)

    while x_rem:
        # work from left-to-right building the result
        # and right-to-left reducing the input parameter

        result = result*10 + (x_rem % 10)
        x_rem = x_rem // 10

    # handles negatives
    return -result if neg else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
