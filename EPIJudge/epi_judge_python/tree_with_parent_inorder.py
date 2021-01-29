from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    prev = None
    result = []
    # print(tree)
    while tree:
        if prev is tree.parent:
            ## came down from prev
            if tree.left:
                next = tree.left
                # prev = tree
                # tree = tree.left
            else:
                result.append(tree.data)
                next = tree.right or tree.parent
                ## cleaner version above, with or short-circuiting
                # if tree.right:
                #     prev = tree
                #     tree = tree.right
                # else:
                #     prev = tree
                #     tree = tree.parent
        # if prev is tree.left:
        ## need to make sure after each case we re-loop, don't re-examine
        ## or else you might run into None errors
        elif prev is tree.left:
            result.append(tree.data)
            next = tree.right or tree.parent
            # if tree.right:
            #     prev = tree
            #     tree = tree.right
            # else:
            #     prev = tree
            #     tree = tree.parent
        # if prev is tree.right:
        else:
            next = tree.parent
            # prev = tree
            # tree = tree.parent
        
        prev, tree = tree, next
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
