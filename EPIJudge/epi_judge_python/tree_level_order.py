from typing import KeysView, List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
#     queue = deque()
#     queue.append(tree)
#     result = []
#     if not tree:
#         return result
#     while queue:
#         next_level: List[BinaryTreeNode] = []
#         key_level: List[int] = []
#         while queue:
#             node = queue.popleft()
#             next_level.append(node)
#             key_level.append(node.data)
#         if key_level:
#             result.append(key_level)
#         for node in next_level:
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
            
            
#     return result

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    curr_depth: List[BinaryTreeNode] = []
    curr_depth.append(tree)
    if not tree:
        return result
    while curr_depth:
        result.append([curr.data for curr in curr_depth])
        curr_depth = [
            child for curr in curr_depth for child in (curr.left, curr.right)
             if child
        ]
    
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
