from test_framework import generic_test


# Returns (carry, result)
def add(x: int, y: int) -> int:
    sm, carry = 0, 0
    tmpx, tmpy = x, y
    k = 1

    while (tmpx | tmpy) != 0:
        xk = x & k
        yk = y & k
        cout = (xk & yk) | (xk & carry) | (yk & carry)

        sm |= (xk ^ yk ^ carry)
        carry = cout << 1
        k <<= 1
        tmpx >>= 1
        tmpy >>= 1
        
    return sm | carry
    

def multiply(x: int, y: int) -> int:
    sm = 0
    while x:
        if (x & 1):
            sm = add(sm, y)
        x >>= 1 # divide by 2
        y <<= 1 # mul by 2

    return sm

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
