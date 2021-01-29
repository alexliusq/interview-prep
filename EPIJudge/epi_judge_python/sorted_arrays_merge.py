from typing import List
import heapq
from collections import namedtuple

from test_framework import generic_test

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    ValueAndArrayMeta = namedtuple('ValueAndArrayMeta', ['value', 'array', 'index'])
    next_heap: List[ValueAndArrayMeta] = []
    result = []
    for index, array in enumerate(sorted_arrays):
        if array:
            heapq.heappush(next_heap, ValueAndArrayMeta(array[0], index, 0))
    while next_heap:
        next = heapq.heappop(next_heap)
        if next.index < len(sorted_arrays[next.array]) - 1:
            new_index = next.index + 1
            heapq.heappush(next_heap, ValueAndArrayMeta(
                sorted_arrays[next.array][new_index], next.array, new_index))
        result.append(next.value)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
