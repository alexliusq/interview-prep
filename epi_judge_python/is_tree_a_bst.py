from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def bst_min_max(tree: BinaryTreeNode) -> Tuple[bool, Tuple[int, int]]:
        if tree.left is None and tree.right is None:
            return (True, (tree.data, tree.data))

        min = tree.data
        max = tree.data
        if tree.left:
            left_is_bst, (left_min, left_max) = bst_min_max(tree.left)
            if not left_is_bst or left_max > tree.data:
                return (False, (0, 0))
            min = left_min
        if tree.right:
            right_is_bst, (right_min, right_max) = bst_min_max(tree.right)
            if not right_is_bst or right_min < tree.data:
                return (False, (0,0))
            max = right_max
        return (True, (min, max))

    if tree is None:
        return True

    return bst_min_max(tree)[0]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
