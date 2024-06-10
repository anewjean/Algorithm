# https://leetcode.com/problems/search-insert-position/
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1 # left와 right에 양 끝의 인덱스를 할당
        while left <= right:
            mid = (left + right) // 2 # 중간값의 인덱스는 left와 right를 더한 값을 2로 나눈 몫
            if nums[mid] == target: # 중간값과 target이 같으면 바로 해당 중간값의 인덱스 반환
                return mid
            elif nums[mid] < target: # 중간값이 타겟보다 작으면 중간값보다 작은 값들은 고려 대상에서 제외
                left = mid + 1
            else:
                right = mid - 1 # 중간값이 타겟보다 크면 중간값보다 큰 값들은 고려 대상에서 제외
        
        return left # left가 right보다 커져서 while문을 빠져나오면 반환