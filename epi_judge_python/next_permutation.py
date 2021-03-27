from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # This algorithm was originally discovered by Narayana Pandita in 14th century AD.
    #
    # Reference:
    #     https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    k, l = 0, 0

    # Step 1
    for i in range(len(perm)-1, 0, -1):
        prev, this = perm[i-1], perm[i]

        if prev < this:
            k = i-1
            break

    else:
        # Last permutation reached
        return []

    # Step 2
    for j in range(len(perm)-1, k, -1):
        elem = perm[j]
        if elem > perm[k]:
            l = j
            break

    else:
        raise Exception("Hit end of 2nd loop with no l value")

    # Step 3
    perm[k], perm[l] = perm[l], perm[k]

    # Step 4
    # Reverse elements [k+1, end]
    elems = perm[k+1:]
    perm = perm[:k+1]
    perm.extend(reversed(elems))

    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
