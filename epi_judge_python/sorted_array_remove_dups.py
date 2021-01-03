import functools
from os import dup
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

## brute force method
## worst case O(n^2) run time 
# def delete_duplicates(A: List[int]) -> int:
#     duplicates = 0
#     idx = 1
#     while idx < len(A):
#         if A[idx] == A[idx - 1]:
#             duplicates += 1
#             del A[idx]
#         else:
#             idx += 1
#     return len(A)

# the worst case performance of the brute force solution is when
# the array is all duplicates, i.e. [1,1,1,1,1] it has to delete and shift n - 1 times
# for a O(n^2) time complexity. instead, have two pointers
# pointer i: the i number to check for duplicates
# [i:] is all unclassified
# pointer total_valid: [:total_valid] all indexes up to and including total_valid are valid
# check if i is duplicate
# if not duplicate, swap with total_valid, increment total valid
# i.e. i = 3, total_valid = 1, [1,1,1,2] -> [1,2,1,1], total_valid = 2
# constant time operation
# return total_valid

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    ## handle special case of array with only one value
    if len(A) == 1:
        return 1
    total_valid = 1
    for i in range(1, len(A)):
        ## test [1,1,2,3,3,4,5,6,6]. i = 1, duplicate
        ## i = 2. valid = 1. not-duplicate. [1,2,1]. valid++
        ## i = 3. valid = 2. not-duplicate. [1,2,3,1]. valid++
        ## i = 4. valid = 3. duplicate. 

        if (A[i] != A[total_valid - 1]):
            if (i != total_valid):
                A[i], A[total_valid] = A[total_valid], A[i]
            total_valid += 1

    return total_valid

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
