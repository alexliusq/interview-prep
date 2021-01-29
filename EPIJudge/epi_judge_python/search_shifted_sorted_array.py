from typing import List

from test_framework import generic_test


# def search_smallest(A: List[int]) -> int:

#     def smallest(A: List[int], start, end) -> int:
#         if start == end:
#             return start

#         if A[start] < A[end]:
#             return start
#         else:
#             middle = (start + end) // 2
#             left_smallest = smallest(A, start, middle)
#             right_smallest = smallest(A, middle + 1, end)
#             if A[left_smallest] <= A[right_smallest]:
#                 return left_smallest
#             else:
#                 return right_smallest

#     start = 0
#     end = len(A) - 1

#     return smallest(A, start, end)

def search_smallest(A: List[int]) -> int:
    ## ALL ELEMENTS ARE DISTINCT
    start = 0
    end = len(A) - 1
    while start < end:
        middle = (start + end) // 2
        if A[middle] > A[end]:
            # min must be in A[mid + 1: end + 1]
            start = middle + 1
        elif A[middle] < A[end]:
            # min can't be in A[mid + 1:], so must be in A[start: mid + 1]
            end = middle
    ## returns when start == end
    return start

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
