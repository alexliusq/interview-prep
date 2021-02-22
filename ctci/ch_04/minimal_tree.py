
from __future__ import annotations
from typing import List

class TreeNode:
    def __init__(self, value: int, left: TreeNode = None, right: TreeNode = None):
        self.value = value
        self.left = left
        self.right = right

    def disp_list(self):
        def in_order(node, depth):
            if not node:
                return
            
            if len(result) <= depth:
                result.append([node.value])
            else:
                result[depth].append(node.value)
            
            in_order(node.left, depth + 1)
            in_order(node.right, depth + 1)
        
        curr = self
        if not curr.value:
            return ''
        result = []
        in_order(curr, 0)
        return '\n'.join(str(x) for x in result)
    
    def disp(self, depth):
        indent = " " * depth * 2
        result = f"{self.value}\n"
        if self.left:
            result += f"{indent}L:"
            result += self.left.disp(depth + 1)
        if self.right:
            result += f"{indent}R:"
            result += self.right.disp(depth + 1)
        return result

    def __str__(self):
        return self.disp(0)

def minimal_tree(d: List[int]) -> TreeNode:
    if not d:
        return None
        
    middle = len(d) // 2
    result = TreeNode(d[middle])
    result.left = minimal_tree(d[:middle])
    result.right = minimal_tree(d[middle + 1:])
    return result

if __name__ == '__main__':
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    # print(a)

    test1 = minimal_tree([i for i in range(20)])
    print(test1)

