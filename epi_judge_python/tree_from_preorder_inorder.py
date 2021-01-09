from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> Optional[BinaryTreeNode]:
    if not preorder:
        return None
        
    root_val = preorder[0]
    root = BinaryTreeNode(root_val)
    in_order_root_index = inorder.index(root_val)

    preorder_left = preorder[1:(1+in_order_root_index)]
    inorder_left = inorder[:in_order_root_index]
    root.left = binary_tree_from_preorder_inorder(preorder_left, inorder_left)

    preorder_right = preorder[(1+in_order_root_index):]
    inorder_right = inorder[(1+in_order_root_index):]
    root.right = binary_tree_from_preorder_inorder(preorder_right, inorder_right)

    return root

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
