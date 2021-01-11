from typing import Iterator

from test_framework import generic_test
from test_framework.test_failure import TestFailure

def find_missing_element(stream: Iterator[int]) -> int:
    candidate_unknowns = [(0, 2**32 - 1)]
    for s in stream:
        for i, unknown in enumerate(candidate_unknowns):
            start, end = unknown
            if s > start and s < end:
                candidate_unknowns[i] = (start, s -1)
                candidate_unknowns.append((s + 1, end))
                break
            if s == start:
                start += 1
            if s == end:
                end -= 1
            if start > end:
                del candidate_unknowns[i]
                break
            else:
                candidate_unknowns[i] = (start, end)
    # print(candidate_unknowns)
    return candidate_unknowns[0][0]


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
