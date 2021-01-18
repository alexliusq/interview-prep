import collections
import functools
from test_framework.serialization_traits import IntegerTrait
from typing import List, Tuple, Dict

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


# def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
#     @functools.cache
#     def enumerate_max(item_index, remaining_weight, prev_value):
#         print(item_index, remaining_weight, prev_value)
#         if item_index == len(items):
#             return prev_value
#         item = items[item_index]
#         max_without = enumerate_max(item_index + 1, remaining_weight, prev_value)
#         if item.weight > remaining_weight:
#             return max_without
#         max_with = enumerate_max(
#             item_index + 1, remaining_weight - item.weight, prev_value + item.value
#         )
#         return max(max_with, max_without)
#     print(items, capacity)
#     return enumerate_max(0, capacity, 0)

def optimum_subject_to_capacity(items:List[Item], capacity: int) -> int:

    def find_max(items: Tuple[Item]) -> int:
        print(len(total_values))
        # print(total_values)
        if total_values.get(items):
            return total_values[items]
        total_weight = total_weights[items]
        if total_weight <= capacity:
            print(total_weight, capacity)
            total_value = sum(value for weight, value in items)
            total_values[items] = total_value
            return total_value
        max_values = []
        for excluded_item in items:
            without_item = tuple(item for item in items if item != excluded_item)
            total_weights[without_item] = total_weight - excluded_item.weight
            max_without = find_max(without_item)
            max_values.append(max_without)

        max_total = max(max_values)
        total_values[items] = max_total
        return max_total
            
    total_values: Dict[Tuple[Item], int] = {}
    total_weights: Dict[Tuple[Item], int] = {}

    total_weights[tuple(items)] = sum(value for weight, value in items)

    for item in items:
        total_values[tuple(item)] = item.value
     
    return find_max(tuple(items))

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
