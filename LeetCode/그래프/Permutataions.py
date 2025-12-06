class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(path):
            # 바닥조건 (순열 완성)
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(path)

                    # 백트래킹
                    path.pop()
                    used[i] = False

        dfs([])
        return res
