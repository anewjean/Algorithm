import heapq

N = int(input())
answer = 0

min_heap = []
for _ in range(N):
    num = int(input())
    heapq.heappush(min_heap, num)
heapq.heapify(min_heap)

while len(min_heap) >= 2:
    first = heapq.heappop(min_heap)
    second = heapq.heappop(min_heap)
    merged = first + second
    answer += merged
    heapq.heappush(min_heap, first + second)

print(answer)