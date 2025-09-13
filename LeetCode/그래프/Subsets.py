class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(idx, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(idx, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return result