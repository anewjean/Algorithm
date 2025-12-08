class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(start):
            # k개를 모두 선택한 경우
            if len(path) == k:
                result.append(path.copy())
                return

            # 남아 있는 숫자가 부족하면 중단
            for num in range(start, n + 1):
                # 선택
                path.append(num)
                dfs(num + 1)
                path.pop() # 백트래킹

        dfs(1)
        return result
