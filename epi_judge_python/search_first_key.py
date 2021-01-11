from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:

    start = 0
    end = len(A) - 1
    result = -1
    while start <= end:
        middle = start + (end - start) // 2
        if A[middle] == k:
            result = middle
            end = middle - 1
        elif A[middle] > k:
            end = middle - 1
        else:
            start = middle + 1

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
