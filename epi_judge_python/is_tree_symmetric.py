from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def check_symmetry(left, right) -> bool:
        # print(left, right)
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.data != right.data:
            return False
        return (check_symmetry(left.left, right.right)
            and check_symmetry(left.right, right.left))
    if not tree:
        return True
    return check_symmetry(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
