class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 0 

        left_depth = self.max_tree(root.left)
        right_depth = self.max_tree(root.right)
        
        return max(left_depth, right_depth) + 1