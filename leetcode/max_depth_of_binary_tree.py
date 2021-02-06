def maxDepth(self, root: TreeNode) -> int:
    def depth_helper(root, depth):
        if not root:
            return depth
        return max(depth_helper(root.left, depth + 1), depth_helper(root.right, depth + 1))
    
    return depth_helper(root, 0)

def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
        
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1