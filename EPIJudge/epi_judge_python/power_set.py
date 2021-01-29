from typing import List

from test_framework import generic_test, test_utils


# def generate_power_set(input_set: List[int]) -> List[List[int]]:

#     def pick_k(prev_set, start_from, k):
#         # print(prev_set, start_from, k)
#         if k == 0:
#             result.append(prev_set)
#             return 
#         iterate_until = len(input_set) - k  + 1
#         for index in range(start_from, iterate_until):
#             next_set = prev_set[:]
#             next_set.append(input_set[index])
#             pick_k(next_set, index + 1, k - 1)

        
#     result = []
#     for i in range(len(input_set) + 1):
#         pick_k([], 0, i)
#     return result

def generate_power_set(input_set: List[int]) -> List[List[int]]:

    def pick_k(prev_set, k, start_from):
        # print(prev_set, start_from, k)
        result.append(prev_set)
        if k == 0:
            return
        for index in range(start_from, min(start_from + k, len(input_set))):
            next_set = prev_set[:]
            next_set.append(input_set[index])
            pick_k(next_set, k - 1, index + 1)
        
    result = []
    pick_k([], len(input_set), 0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
