# https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
def countPairs(self, nums: List[int], target: int) -> int:
    nums.sort()
    answer = 0
    left = 0 # nums의 첫 번째 요소의 인덱스
    right = len(nums) - 1 # nums의 마지막 요소의 인덱스(nums 요소의 개수에서 1을 뺀 값)

    while left < right:
        if nums[left] + nums[right] < target: # nums[left] + nums[right] < target 조건을 만족한다면 
            answer += (right - left) # answer에 오른쪽 포인터가 가리키는 인덱스에서 왼쪽 포인터가 가리키는 인덱스를 뺀 값을 더함
            left += 1 # 왼쪽 포인터를 한 칸 오른쪽으로 이동
        else: # 조건을 만족하지 않는다면 오른쪽 포인터를 한 칸 왼쪽으로 이동
            right -= 1

    return answer