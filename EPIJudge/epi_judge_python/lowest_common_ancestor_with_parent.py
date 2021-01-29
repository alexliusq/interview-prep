import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import convert_binary_tree_to_binary_tree_with_parent, must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    def get_height(node: BinaryTreeNode) -> int:
        height = 0
        while node.parent:
            height += 1
            node = node.parent
        return height

    if not node0 or not node1:
        return None

    node0_height = get_height(node0)
    node1_height = get_height(node1)
    longer = node0 if node0_height >= node1_height else node1
    shorter = node0 if node0_height < node1_height else node1
    for _ in range(abs(node0_height - node1_height)):
        longer = longer.parent
    while shorter is not longer:
        shorter = shorter.parent
        longer = longer.parent
    return shorter


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
