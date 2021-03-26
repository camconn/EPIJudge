from test_framework import generic_test


INT_SIZE = 64

def closest_int_same_bit_count(x: int) -> int:
    for i in range(INT_SIZE):
        if ((x >> i) & 1) != ((x >> (i+1)) & 1):
            x ^= (1 << i) | (1 << (i+1))
            return x
    
    assert(False, "Invalid case")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
