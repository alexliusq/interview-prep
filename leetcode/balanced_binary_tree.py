
def isBalanced(root: TreeNode) -> bool:
    def balance_helper(root):
        if not root:
            return (True, 0)
        left_balanced, left_height = balance_helper(root.left)
        right_balanced, right_height = balance_helper(root.right)
        if not (left_balanced and right_balanced):
            return (False, 0)
        if abs(left_height - right_height) > 1:
            return (False, 0)
        
        return (True, max(left_height, right_height) + 1)
        
    return balance_helper(root)[0]