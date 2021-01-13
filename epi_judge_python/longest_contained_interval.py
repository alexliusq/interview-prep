from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    candidates = set(A)
    range_lengths = []
    for num in A:
        if not candidates:
            break
        if num not in candidates:
            continue
        range_length = 1
        left = right = num
        candidates.remove(num)
        while (left - 1) in candidates:
            left = left - 1
            range_length += 1
            candidates.remove(left)
        while (right + 1) in candidates:
            right = right + 1
            range_length += 1
            candidates.remove(right)
        range_lengths.append(range_length)
        
    return max(range_lengths)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
