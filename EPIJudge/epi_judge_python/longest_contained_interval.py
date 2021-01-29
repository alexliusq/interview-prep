from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    candidates = set(A)
    max_range = 0
    while candidates:
        num = candidates.pop()
        range_length = 1
        left = right = num
        while (left - 1) in candidates:
            left = left - 1
            range_length += 1
            candidates.remove(left)
        while (right + 1) in candidates:
            right = right + 1
            range_length += 1
            candidates.remove(right)
        max_range = max(max_range, range_length)
        
    return max_range


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
