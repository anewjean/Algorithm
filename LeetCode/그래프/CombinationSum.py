class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return

            # 실패 조건: 인덱스를 벗어나거나 합이 초과되는 경우
            if i >= len(candidates) or total > target:
                return

            # 1) 현재 값을 선택하는 경우
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()

            # 2) 현재 값을 건너뛰고 다음 숫자로 이동
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
