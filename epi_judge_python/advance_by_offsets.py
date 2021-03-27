from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    i = 0
    max_pos = 0
    current = A[i]

    # Edge case
    if len(A) <= 1:
        return True

    while i < len(A) and i <= max_pos:
        current = A[i]
        target = i + current

        max_pos = max(max_pos, target)

        # If we are the farthest we can go, and have reached the end.
        if max_pos == i and max_pos < len(A)-1:
            return False

        i += 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
