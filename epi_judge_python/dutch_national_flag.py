import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


# def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
#     center_value = A[pivot_index]
#     next_pivot = 0
#     num_equals = 0
#     next_greater = len(A) - 1
#     while (next_pivot <= next_greater):
#         # print(f'p{next_pivot} e{num_equals} g{next_greater}')
#         if (A[next_pivot] < center_value):
#             if (num_equals > 0):
#                 A[next_pivot], A[next_pivot - num_equals] = A[next_pivot - num_equals], A[next_pivot]
#             next_pivot += 1
#         elif (A[next_pivot] == center_value):
#             next_pivot += 1
#             num_equals += 1
#         else:
#             A[next_pivot], A[next_greater] = A[next_greater], A[next_pivot]
#             next_greater -= 1
#     return A

# two pass method
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]
    smaller = -1
    larger = len(A)
    for i in range(len(A)):
        if (A[i] < pivot):
            smaller += 1
            A[smaller], A[i] = A[i], A[smaller]
    for i in reversed(range(len(A))):
        if (A[i] < pivot):
            break
        if (A[i] > pivot):
            larger -= 1
            A[larger], A[i] = A[i], A[larger]
    return A

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
