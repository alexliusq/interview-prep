from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    iter_a = 0
    iter_b = 0
    result = []
    while iter_a < len(A) and iter_b < len(B):
        # if iter_a < len(A) - 1 and A[iter_a] == A[iter_a + 1]:
        #     iter_a += 1
        #     continue

        # if iter_b < len(B) - 1 and B[iter_b] == B[iter_b + 1]:
        #     iter_b += 1
        #     continue

        if A[iter_a] == B[iter_b]:
            if iter_a == 0 or A[iter_a] != A[iter_a - 1]:
                result.append(A[iter_a])
            iter_a += 1
            iter_b += 1
        elif A[iter_a] < B[iter_b]:
            iter_a += 1
        else:
            ## case A[iter_a] > B[iter_b]
            iter_b+=1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
