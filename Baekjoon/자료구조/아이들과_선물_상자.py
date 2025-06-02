import heapq

N, M = map(int, input().split())
boxes = list(map(int, input().split()))
children_hopes = list(map(int, input().split()))

boxes = [-x for x in boxes]
heapq.heapify(boxes)

answer = 1
for child_hope in children_hopes:
    max_count = -heapq.heappop(boxes)
    if max_count < child_hope:
        answer = 0
        break
    leftover = max_count - child_hope
    heapq.heappush(boxes, -leftover)

print(answer)