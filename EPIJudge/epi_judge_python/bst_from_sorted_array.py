import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
#     if not A:
#         return None
#     middle = len(A) // 2
#     node = BstNode(A[middle])
#     node.left = build_min_height_bst_from_sorted_array(A[:middle])
#     ## exploits python list slicing return empty subarray if out of range
#     node.right = build_min_height_bst_from_sorted_array(A[middle+1:])
#     return node

## solution with O(1) space, O(n) time
def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    def bst_helper(A, start, end):
        if end < start:
            return None
        middle = (start + end) // 2
        node = BstNode(A[middle])
        node.left = bst_helper(A, start, middle - 1)
        node.right = bst_helper(A, middle + 1, end)
        return node

    if not A:
        return None
    return bst_helper(A, 0, len(A) - 1)

@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))