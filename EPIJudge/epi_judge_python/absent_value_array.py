from typing import Counter, Iterator
import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure

## Your code works and is based on keeping a set of candidate ranges that
## could contain unknowns. however with array probably terribly inefficent
## even with a linked list which provides O(1) insertion and O(1) deletion
## it would take O(n) search to find the right range
## can't just use a hash table because it's ranges not exact keys
## BST would probably be best 
##
# def find_missing_element(stream: Iterator[int]) -> int:
#     candidate_unknowns = [(0, 2**32 - 1)]
#     for s in stream:
#         for i, unknown in enumerate(candidate_unknowns):
#             start, end = unknown
#             if s > start and s < end:
#                 candidate_unknowns[i] = (start, s -1)
#                 candidate_unknowns.append((s + 1, end))
#                 break
#             if s == start:
#                 start += 1
#             if s == end:
#                 end -= 1
#             if start > end:
#                 del candidate_unknowns[i]
#                 break
#             else:
#                 candidate_unknowns[i] = (start, end)
#     # print(candidate_unknowns)
#     return candidate_unknowns[0][0]

def find_missing_element(stream: Iterator[int]) -> int:
    num_bucket = 1 << 16
    msb_count = [0] * num_bucket
    stream_copy, stream = itertools.tee(stream, 2)
    for x in stream:
        msb_x = x >> 16
        msb_count[msb_x] += 1
    
    bucket_capacity = 1 << 16
    candidate_bucket = next(i for i, c in enumerate(msb_count)
                            if c < bucket_capacity)

    candidates = [0] * bucket_capacity
    for x in stream_copy:
        msb_x = x >> 16
        if candidate_bucket == msb_x:
            lsb_x = ((1 << 16) - 1) & x
            candidates[lsb_x] = 1
    
    for i, v in enumerate(candidates):
        if v == 0:
            return (candidate_bucket << 16) | i
    
    raise ValueError('no missing element')


def find_missing_element_wrapper(stream):
    try:
        res = find_missing_element(iter(stream))
        if res in stream:
            raise TestFailure('{} appears in stream'.format(res))
    except ValueError:
        raise TestFailure('Unexpected no missing element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('absent_value_array.py',
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
