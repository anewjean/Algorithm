class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def backtrack(start):
            res.append(subset[:])

            for i in range(start, len(nums)):
                # 같은 depth에서 중복 스킵
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res
