# https://leetcode.com/problems/range-sum-of-bst/description/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def range_sum_BST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        answer = 0
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    answer += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return answer