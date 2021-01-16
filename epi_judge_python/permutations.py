from typing import List

from test_framework import generic_test, test_utils


# def permutations(A: List[int]) -> List[List[int]]:
#     def next_permutation(A: List[int], permutation: List[int], permutation_length):
#         # print(A)
#         if not A:
#             result.append(list(permutation))
#             return 
#         for idx, num in enumerate(A):
#             permutation[permutation_length] = num
#             shrunk_a = A[:idx] + A[idx + 1:]
#             next_permutation(shrunk_a, permutation, permutation_length + 1)

#     result = []
#     permutation = [0] * len(A)
#     next_permutation(A, permutation, 0)
#     return result

## the cleaner, O(1) space solution
def permutations(A: List[int]) -> List[List[int]]:
    def next_permutation(index):
        if index == len(A) - 1:
            result.append(A.copy())
            return
        for next_start in range(index, len(A)):
            A[next_start], A[index] = A[index], A[next_start]
            next_permutation(index + 1)
            ## swap it back after it's all done. pretty genius
            A[index], A[next_start] = A[next_start], A[index]

    result = []
    next_permutation(0)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
