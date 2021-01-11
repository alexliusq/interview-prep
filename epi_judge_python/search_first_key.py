from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    def binary_search(a: List[int], target, start, end) -> int:
        if start < 0 or end > len(a) - 1:
            return -1
        while start <= end:
            middle = start + (end - start) // 2
            if a[middle] == target:
                return middle
            elif a[middle] > target:
                end = middle - 1
            else:
                start = middle + 1
    
        return -1
    
    prev_hit = next_hit = binary_search(A, k, 0, len(A) - 1)
    while next_hit > -1:
        prev_hit = next_hit
        next_hit = binary_search(A, k, 0, prev_hit - 1)

    return prev_hit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
