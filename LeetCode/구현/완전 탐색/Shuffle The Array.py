from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i // 2 + (i % 2) * n] for i in range(2 * n)] # 짝수 인덱스인 경우 nums[i//2], 홀수 인덱스인 경우 nums[i//2 + n]