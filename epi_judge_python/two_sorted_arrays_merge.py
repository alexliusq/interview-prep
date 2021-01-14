from decimal import Inexact
from typing import List

from test_framework import generic_test
from collections import deque

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    iter_b = 0
    temp_storage = deque()
    for i in range(m):
        temp_storage.append(A[i])
    iter_b = 0
    for index in range(len(A)):
        if temp_storage and iter_b < n:
            if temp_storage[0] < B[iter_b]:
                A[index] = temp_storage.popleft()
            else:
                A[index] = B[iter_b]
                iter_b += 1
        elif temp_storage:
            A[index] = temp_storage.popleft()
        else:
            A[index] = B[iter_b]
            iter_b += 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
