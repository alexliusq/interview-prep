from typing import Iterator, List
from test_framework import generic_test

import heapq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    next_k: List[int] = []
    result = []
    for _ in range(k):
        next_val = next(sequence, None)
        if next_val is not None:
            heapq.heappush(next_k, next_val)
    while next_k:
        result.append(heapq.heappop(next_k))
        next_val = next(sequence, None)
        if next_val is not None:
            heapq.heappush(next_k, next_val)

    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
