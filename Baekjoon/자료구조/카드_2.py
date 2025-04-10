from collections import deque

N = int(input())
queue = deque()

for i in range(1, N+1):
    queue.appendleft(i)

while len(queue) > 1:
    queue.pop()
    queue.appendleft(queue.pop())
print(*queue)