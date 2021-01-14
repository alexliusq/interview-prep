import collections
from decimal import ROUND_05UP
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    def larger_right(interval0: Interval, interval1: Interval) -> Endpoint:
        if interval0.right.val > interval1.right.val:
            return interval0.right
        elif interval1.right.val > interval0.right.val:
            return interval1.right
        else: ## interval0.right.val == interval1.right.val
            if interval1.right.is_closed or interval0.right.is_closed:
                return Endpoint(True, interval0.right.val)
            else:
                return Endpoint(False, interval0.right.val)

    intervals.sort(key =lambda x:
                   (x.left.val, not x.left.is_closed, x.right, not x.right.is_closed)
                   )
    # print([(x.left.val, x.left.is_closed) for x in intervals])
    if not intervals:
        return []
    result = [intervals[0]]
    iter = 0
    for iter in range(1, len(intervals)):
        union = result[-1]
        curr = intervals[iter]
        # print('curr', curr)
        # print('union', union)
        if curr.left.val < union.right.val:
            result[-1] = Interval(union.left, larger_right(union, curr))
        elif (curr.left.val == union.right.val and
            (curr.left.is_closed or union.right.is_closed)
            ):
            result [-1] = Interval(union.left, larger_right(union, curr))
        else:
            result.append(curr)

    return result


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
