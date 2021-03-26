import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# naive solution
# O(n²)
#def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
#    low, middle, high = 0, 0, 0
#    pivot = A[pivot_index]
#
#    for i in range(len(A)):
#        for j in range(i+1, len(A)):
#            after = A[j]
#            if after < pivot:
#                A[i], A[j] = A[j], A[i]
#                break
#
#    for i in range(len(A)-1, -1, -1):
#        if A[i] < pivot:
#            break
#
#        for j in range(i-1, -1, -1):
#            before = A[j]
#
#            if before < pivot:
#                break
#
#            if before > pivot:
#                A[i], A[j] = A[j], A[i]
#                break

# Efficient way
# O(n)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    larger = len(A) - 1
    for i in range(len(A)-1, -1, -1):
        if A[i] < pivot: break

        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
