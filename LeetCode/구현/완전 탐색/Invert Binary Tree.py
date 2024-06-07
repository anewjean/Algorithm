class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
            
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.right, root.left = root.left, root.right # 왼쪽 노드에는 오른 노드를 할당, 오른쪽 노드에는 왼쪽 노드를 할당

        return root