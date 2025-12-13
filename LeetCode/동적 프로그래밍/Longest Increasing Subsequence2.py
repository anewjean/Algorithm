import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        
        for num in nums:
            # tails에서 num이 들어갈 위치 찾기
            idx = bisect.bisect_left(tails, num)
            
            # 새로운 subsequence
            if idx == len(tails):
                tails.append(num)
            # 기존 tail 값 교체
            else:
                tails[idx] = num
        
        return len(tails)
