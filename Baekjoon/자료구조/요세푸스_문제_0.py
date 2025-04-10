from collections import deque

N, K = map(int, input().split())

queue = deque()

for i in range(1, N + 1):
    queue.appendleft(i)

jump = K-1
answer = []
while queue:
    queue.rotate(jump)
    answer.append(str(queue.pop()))

print(f"<{', '.join(answer)}>")

