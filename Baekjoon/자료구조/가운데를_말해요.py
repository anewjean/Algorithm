N = int(input())
nums = []
# for _ in range(N):
#     nums.append(int(input()))
#     nums.sort()
#     if len(nums) % 2 == 0:
#         mid = len(nums) - (len(nums) // 2 + 1)
#     else:
#         mid = len(nums) - len(nums) // 2 - 1
#     print(nums[mid])



import heapq

min_heap = [] # 중간값 초과 요소들
max_heap = [] # 중간값 이하 요소들

for i in range(N):
    num = int(input())
    heapq.heappush(max_heap, -num) # 새로운 요소가 들어오면 max_heap에 넣는다

    if min_heap and -max_heap[0] > min_heap[0]:
        above_mid = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, above_mid)

    # -max_heap[0]이 항상 중간값이 되도록 유지
    # 총 입력 개수가 홀수일 때??? max_heap에 하나가 더 많도록 개수 유지
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    # 총 입력 개수가 짝수일 때??? min_heap, max_heap 크기가 동일하게 유지
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    print(-max_heap[0])
