from typing import Iterator, List

from test_framework import generic_test

import heapq

def online_median(sequence: Iterator[float]) -> List[float]:
    left_max = []
    right_min = []
    result: List[float] = []
    
    first_val = next(sequence, None)
    if first_val is None:
        return result
    result.append(first_val)
    second_val = next(sequence, None)
    if second_val is None:
        return result
    if first_val <= second_val:
        left_max.append(-first_val)
        right_min.append(second_val)
    else:
        left_max.append(-second_val)
        right_min.append(first_val)
    result.append((first_val+second_val) / 2)
    for s in sequence:
        # print('result', result)
        # print('left max',  left_max)
        # print('right_min', right_min)
        if s <= right_min[0]:
            heapq.heappush(left_max, -s)
            if len(left_max) - len(right_min) > 1:
                heapq.heappush(right_min, -heapq.heappop(left_max))
        else:
            heapq.heappush(right_min, s)
            if len(right_min) - len(left_max) > 1:
                heapq.heappush(left_max, -heapq.heappop(right_min))

        if len(left_max) == len(right_min):
            ## both left and right are equal lenght
            result.append((-left_max[0] + right_min[0])/2)
        elif len(left_max) > len(right_min):
            result.append(-left_max[0])
        else:
            result.append(right_min[0])

    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
