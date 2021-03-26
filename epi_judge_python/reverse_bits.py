from test_framework import generic_test

import sys

def reverse_bits(x: int) -> int:
    # assume integer size of 64 bits for compatibility with tests
    size = 64

    binary = ''.join(reversed(bin(x)))
    binary = binary[:-2]
    rev = ''.join(binary)
    rev = rev + '0'*(size - len(rev))
    result = int(rev, base=2)
    return int(rev, 2)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
