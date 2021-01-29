from decimal import Inexact
from typing import List

from test_framework import generic_test
from collections import deque

# def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
#                             n: int) -> None:
#     iter_b = 0
#     temp_storage = deque()
#     for i in range(m):
#         temp_storage.append(A[i])
#     iter_b = 0
#     for index in range(len(A)):
#         if temp_storage and iter_b < n:
#             if temp_storage[0] < B[iter_b]:
#                 A[index] = temp_storage.popleft()
#             else:
#                 A[index] = B[iter_b]
#                 iter_b += 1
#         elif temp_storage:
#             A[index] = temp_storage.popleft()
#         else:
#             A[index] = B[iter_b]
#             iter_b += 1
#     return

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    end = m + n - 1
    iter_a = m - 1
    iter_b = n - 1
    while end >= 0:
        if iter_a >= 0 and iter_b >= 0:
            if A[iter_a] > B[iter_b]:
                A[end] = A[iter_a]
                iter_a -= 1
            else:
                A[end] = B[iter_b]
                iter_b -= 1
        elif iter_b >= 0:
            A[end] = B[iter_b]
            iter_b -= 1
        else: ## iter_a >= 0
            A[end] = A[iter_a]
            iter_a -= 1
        # print(A)
        end -= 1



def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
