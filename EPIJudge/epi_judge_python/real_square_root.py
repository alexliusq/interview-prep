import math
from os import kill
from test_framework import generic_test


# def square_root(x: float) -> float:
#     inverse = False
#     if x < 1:
#         x = 1/x
#         inverse = True
#     start = 0.0
#     end = x
#     print(x)
#     while start <= end:
#         middle = (start + end) / 2
#         # print('start', start, 'end', end, 'middle', middle)
#         if math.isclose(middle ** 2, x):
#             if inverse:
#                 return 1 / middle
#             return middle
#         if middle ** 2 > x:
#             end = math.nextafter(middle, 0)
#         else:
#             start = math.nextafter(middle, x)
#     result = math.nextafter(start, 0)
#     if inverse:
#         return 1 / result
#     return result

def square_root(x: float) -> float:
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    while not math.isclose(left, right):
        mid = 0.5 * (left + right)
        mid_squared = mid ** 2
        if mid_squared > x:
            right = mid
        else:
            left = mid
    return left

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
