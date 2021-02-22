from __future__ import annotations

from minimal_tree import TreeNode, minimal_tree

from typing import List

class ListNode:
    def __init__(self, value, next: ListNode = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(curr.value)
            curr = curr.next
        return ' -> '.join(str(value) for value in result)
    


def list_of_depths(r: TreeNode) -> List[ListNode]:
    def pre_order(r: TreeNode, depth: int):
        if not r:
            return

        node = ListNode(r.value)
        if depth >= len(result):
            head = tail = node
            result.append([head, tail])
        else:
            result[depth][1].next = node
            result[depth][1] = node
        
        pre_order(r.left, depth + 1)
        pre_order(r.right, depth + 1)


    result = []
    pre_order(r, 0)
    return [head for head, _ in result]

tree = minimal_tree([i for i in range(20)])
print(tree)
depths = list_of_depths(tree)
for i, node in enumerate(depths):
    print(i, ': ', node)