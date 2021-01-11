from os import EX_DATAERR
from typing import List
import random

from test_framework import generic_test

def partial_sort(A, start, end, pivot_index) -> int:
    pivot = A[pivot_index]
    A[end], A[pivot_index] = A[pivot_index], A[end]
    left, right = start, end
    ## loop invariant:
    ## [:left] is less than pivot
    ## [right:] greater than or equal to pivot
    # print(pivot)
    while left < right:
        if A[left] < pivot:
            left += 1
        else:
            right -= 1
            A[left], A[right] = A[right], A[left]
    # print('A', A)
    A[right], A[end] = A[end], A[right]
    # print('right', right)
    # print(A)
    return right

# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    start = 0
    end = len(A) - 1
    # print(A)
    # print(potential_k)
    target_k = len(A) - k
    while (start <= end):
        pivot_index = random.randint(start, end)
        potential_k = partial_sort(A, start, end, pivot_index)
        if potential_k == target_k:
            return A[potential_k]
        elif potential_k < target_k:
            start = potential_k + 1
        else:
            end = potential_k - 1

    raise IndexError('no k-th node')


if __name__ == '__main__':
    # a = list(range(10, 0, -1))
    # partial_sort(a, 0, 9)
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))