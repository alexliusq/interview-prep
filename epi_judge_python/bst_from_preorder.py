from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    if not preorder_sequence:
        return None
    current_val = preorder_sequence[0]
    node = BstNode(current_val)

    
    
    idx_greater_than = None
    for idx, num in enumerate(preorder_sequence):
        if num > current_val:
            idx_greater_than = idx
            break
    
    if idx_greater_than:
        node.left = rebuild_bst_from_preorder(
            preorder_sequence[1:idx_greater_than]
        )
        node.right = rebuild_bst_from_preorder(
            preorder_sequence[idx_greater_than:]
        )
    else:
        node.left = rebuild_bst_from_preorder(
            preorder_sequence[1:]
        )
    return node


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
