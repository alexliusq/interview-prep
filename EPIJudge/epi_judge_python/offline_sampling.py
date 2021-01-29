import functools
from typing import List

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import random

# def random_sampling(k: int, A: List[int]) -> None:
#     # print(A, k, sep=', ')
#     last_index = len(A) - 1
#     num_delete = len(A) - k
#     delete_to = last_index - num_delete
#     # print(f'end{last_index}, delete until {delete_to}')
#     # print(list(range(last_index, delete_to, -1)))
#     for i in range(last_index, delete_to, -1):
#         delete_idx = random.randint(0, i)
#         # print(f'rand int {delete_idx}')
#         del A[delete_idx]
#     # print(A)

def random_sampling(k: int, A: List[int]) -> None:
    end_idx = len(A) - 1
    for i in range (k):
        choice = random.randint(i, end_idx)
        A[i], A[choice] = A[choice], A[i]


@enable_executor_hook
def random_sampling_wrapper(executor, k, A):
    def random_sampling_runner(executor, k, A):
        result = []

        def populate_random_sampling_result():
            for _ in range(100000):
                random_sampling(k, A)
                result.append(A[:k])

        executor.run(populate_random_sampling_result)

        total_possible_outcomes = binomial_coefficient(len(A), k)
        A = sorted(A)
        comb_to_idx = {
            tuple(compute_combination_idx(A, len(A), k, i)): i
            for i in range(binomial_coefficient(len(A), k))
        }

        return check_sequence_is_uniformly_random(
            [comb_to_idx[tuple(sorted(a))] for a in result],
            total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_sampling_runner, executor, k, A))


if __name__ == '__main__':
    # test_list = [1,2,3,4]
    # random_sampling(1, test_list)
    # print(test_list)
    exit(
        generic_test.generic_test_main('offline_sampling.py',
                                       'offline_sampling.tsv',
                                       random_sampling_wrapper))
