from typing import List

from test_framework import generic_test


# def has_three_sum(A: List[int], t: int) -> bool:
#     # TODO - you fill in here.
#     pair_dict = {}
#     for i in range(len(A)):
#         for j in range(i ,len(A)):
#             sum = A[i] + A[j]
#             pair_dict[sum] = [A[i], A[j]]
#     for num in A:
#         if pair_dict.get(t - num):
#             return True
#     return False

def has_two_sum(A: List[int], target_sum: int) -> bool:
    i = 0
    j = len(A) - 1
    while i <= j:
        pair_sum = A[i] + A[j]
        if pair_sum == target_sum:
            return True
        elif pair_sum > target_sum:
            j -= 1
        else: # pair sum < target_sum
            i += 1

def has_three_sum(A: List[int], t: int) -> bool:
    # TODO - you fill in here.
    A.sort()
    for num in A:
        if has_two_sum(A, t - num):
            return True
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
