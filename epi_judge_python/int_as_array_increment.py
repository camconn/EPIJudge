from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    last = len(A) - 1
    A[last] += 1

    for i in range(len(A) - 1, -1, -1):
        num = A[i]
        if num >= 10:
            A[i] = num % 10

            if i >= 1:
                # If there is a number before this one
                A[i-1] += 1
            else:
                A.insert(0, 1)
    return A
        


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
