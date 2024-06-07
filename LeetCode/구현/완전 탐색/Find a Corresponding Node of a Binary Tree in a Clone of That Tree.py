class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_target_copy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 오리지널 트리가 비어있으면 복제된 트리도 비어있으므로 None 반환
        if original is None:
            return
        
        # 오리지널의 노드와 타겟이 같으면 복제된 트리의 노드 반환
        if original == target:
            return cloned
        
        # 루트 기준 왼쪽 서브트리에서 재귀적으로 탐색
        left_of_cloned = self.get_target_copy(original.left, cloned.left, target)
        if left_of_cloned:
            return left_of_cloned
        
        # 루트 기준 오른쪽 서브트리에서 재귀적으로 탐색
        right_of_cloned = self.get_target_copy(original.right, cloned.right, target)
        if right_of_cloned:
            return right_of_cloned
        
        # 왼쪽, 오른쪽 서브트리 모두에서 노드를 발견하지 못 하면 None 반환
        return