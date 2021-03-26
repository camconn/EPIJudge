from test_framework import generic_test


LUT = dict()

def _parity(x: int) -> int:
    count = 0

    while x != 0:
        count += 1
        x &= (x-1)

    return count % 2

for i in range(2**16):
    LUT[i] = _parity(i)

def parity(x: int) -> int:
    pty = 0

    while x != 0:
        byt = x & 0xffff # take last 16 bits

        pty ^= LUT[byt]
        x = x >> 16

    return pty




if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
