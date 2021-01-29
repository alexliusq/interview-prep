from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    left = max_left = 0
    right = max_right = len(heights) - 1
    max_water = min(heights[max_left], heights[max_right]) * (max_right - max_left)

    while right > left:
        if heights[right] <= heights[left]:
            right -= 1
        else:
            left += 1
        
        new_max = min(heights[left], heights[right]) * (right - left)
        if new_max > max_water:
            max_water = new_max
            max_left = left
            max_right = right
    # print(max_left, max_right)
    return max_water


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
