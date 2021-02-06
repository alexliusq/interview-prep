class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: TreeNode) -> bool:
    def bst_helper(root: TreeNode):
        if not root:
            return (True, (0,0))
        
        current_range = [root.val, root.val]
        
        if root.left:
            if not (root.left.val < root.val):
                return (False, (0,0))
            left_is_valid, left_range = bst_helper(root.left)
            if not left_is_valid:
                return (False, (0,0))
            if not (left_range[1] < root.val):
                return (False, (0,0))
            current_range[0] = left_range[0]
        
        if root.right:
            if not (root.right.val > root.val):
                return (False, (0,0))
            right_is_valid, right_range = bst_helper(root.right)
            if not right_is_valid:
                return (False, (0,0))
            if not (right_range[0] > root.val):
                return (False, (0,0))
            current_range[1] = right_range[1]
        
        return (True, tuple(current_range))
    
    valid_bst, _ = bst_helper(root)
    return valid_bst

def isValidBST(root: TreeNode) -> bool:
    def bst_helper(root: TreeNode, floor, ceiling):
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return (bst_helper(root.left, floor, root.val) and
        bst_helper(root.right, root.val, ceiling))
    
    return bst_helper(root, float('-inf'), float('inf'))