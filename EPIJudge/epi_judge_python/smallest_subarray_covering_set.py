import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

from collections import OrderedDict

def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    smallest_cover = Subarray(0,len(paragraph))
    keyword_locations = OrderedDict()
    # print('NEW')
    for index, word in enumerate(paragraph):
        if word in keywords:
            if word in keyword_locations:
                del keyword_locations[word]
            keyword_locations[word] = index
            # print(list(keyword_locations.items()))
        if len(keyword_locations) == len(keywords):
            locations = list(keyword_locations.values())
            # print(locations)
            start = locations[0]
            end = locations[-1]
            # print(start, end)
            current_cover_length = smallest_cover.end - smallest_cover.start
            if end - start < current_cover_length:
                smallest_cover = Subarray(start, end)
    
    return smallest_cover


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
