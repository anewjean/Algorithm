class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
            # 리프 노드인 경우 그 값(0 또는 1)을 반환
            if root.left is None and root.right is None:
                return root.val == 1
            
            # 왼쪽 자식과 오른쪽 자식을 재귀적으로 평가
            left_eval = self.evaluateTree(root.left)
            right_eval = self.evaluateTree(root.right)
            
            # 현재 노드의 값이 2인 경우 OR 연산 수행
            if root.val == 2:
                return left_eval or right_eval
            # 현재 노드의 값이 3인 경우 AND 연산 수행
            elif root.val == 3:
                return left_eval and right_eval