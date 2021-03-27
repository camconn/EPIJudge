import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    j = 1
    remove = 0

    # move dupes to end
    for i in range(1, len(A)):
        current = A[i]
        
        if current == A[j-1]:
            # duplicates
            # just iterate item index
            remove += 1
            continue

        # not duplicates
        A[j] = current

        j += 1

    for _ in range(remove):
        A.pop()

    return len(A)


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
