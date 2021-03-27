import copy
import functools
import math
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import functools
import itertools
import random
import math



@functools.lru_cache(maxsize=2048)
def fact(n):
    return math.factorial(n)
    

# First attempt, brute-force approach.
def _compute_random_permutation(n: int) -> List[int]:
    if n == 1:
        return [0]

    possible = fact(n)

    num = random.randint(1, possible)

    nums = list(range(n))

    perms = itertools.permutations(nums)
    for i in range(possible):
        if i+1 == num:
            return list(next(perms))
        next(perms)

    return None

def compute_random_permutation(n: int) -> List[int]:
    sample = list(range(n))

    # Knuth Shuffle
    for i in range(n):
        target = random.randint(i, n-1)
        sample[i], sample[target] = sample[target], sample[i]

    return sample


@enable_executor_hook
def compute_random_permutation_wrapper(executor, n):
    def compute_random_permutation_runner(executor, n):
        def permutation_index(perm):
            p = copy.deepcopy(perm)
            idx = 0
            n = len(p)
            while p:
                a = p.pop(0)
                idx += a * math.factorial(n - 1)
                for i, b in enumerate(p):
                    if b > a:
                        p[i] -= 1
                n -= 1
            return idx

        result = executor.run(
            lambda: [compute_random_permutation(n) for _ in range(1000000)])

        return check_sequence_is_uniformly_random(
            [permutation_index(perm) for perm in result], math.factorial(n),
            0.01)

    run_func_with_retries(
        functools.partial(compute_random_permutation_runner, executor, n))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('random_permutation.py',
                                       'random_permutation.tsv',
                                       compute_random_permutation_wrapper))
