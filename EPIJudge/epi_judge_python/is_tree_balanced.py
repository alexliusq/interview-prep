from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from typing import Tuple

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # print(tree)
    if not tree:
        return True
    
    return check_balance(tree)[0]

def check_balance(root: BinaryTreeNode) -> Tuple[bool, int]:
    root_left = root_right = -1
    # print(root.data)
    if root.left:
        balanced, root_left = check_balance(root.left)
        if not balanced:
            return (False, -1)
    if root.right:
        balanced, root_right = check_balance(root.right)
        if not balanced:
            return (False, -1)
    larger = root_left if root_left > root_right else root_right
    return (abs(root_left - root_right) <= 1, larger + 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
