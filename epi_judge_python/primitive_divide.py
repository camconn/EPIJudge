from test_framework import generic_test


def divide(x: int, y: int) -> int:
    res = 0
    pwr = 32

    y_pow = y << pwr
    while x >= y:
        while y_pow > x:
            y_pow >>= 1
            pwr -= 1

        res += 1 << pwr
        x -= y_pow
    
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
