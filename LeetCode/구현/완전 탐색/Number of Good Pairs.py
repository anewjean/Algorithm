from typing import List
from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0 # 'nums[i] == nums[j] and i < j'를 만족하는 (i, j) 쌍 개수
        count = defaultdict(int) # num을 키로, num이 반복되는 횟수를 값으로 가지는 딕셔너리
        
        for num in nums:
            good_pairs += count[num]
            count[num] += 1
        
        return good_pairs