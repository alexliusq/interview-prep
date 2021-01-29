from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


# def rebuild_bst_from_preorder(preorder_sequence: List[int]
#                               ) -> Optional[BstNode]:
    # if not preorder_sequence:
    #     return None
    # current_val = preorder_sequence[0]
    # node = BstNode(current_val)

    
    
    # idx_greater_than = None
    # for idx, num in enumerate(preorder_sequence):
    #     if num > current_val:
    #         idx_greater_than = idx
    #         break
    
    # if idx_greater_than:
    #     node.left = rebuild_bst_from_preorder(
    #         preorder_sequence[1:idx_greater_than]
    #     )
    #     node.right = rebuild_bst_from_preorder(
    #         preorder_sequence[idx_greater_than:]
    #     )
    # else:
    #     node.left = rebuild_bst_from_preorder(
    #         preorder_sequence[1:]
    #     )
    # return node

## efficient O(n), O(1) space algo
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def preorder_helper(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None
        root = preorder_sequence[root_idx[0]]
        if not lower_bound <= root <= upper_bound:
            return None
        root_idx[0] += 1
        node = BstNode(root)
        ## ordering is critical
        node.left = preorder_helper(lower_bound, root)
        node.right = preorder_helper(root, upper_bound)
        return node

    root_idx = [0]
    return preorder_helper(float('-inf'), float('inf'))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
