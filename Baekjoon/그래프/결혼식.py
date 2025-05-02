from collections import deque

n = int(input())
m = int(input())
relations = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

count = 0
visited = [False] * (n+1)
visited[1] = True
q = deque()
q.append((1, 0)) # (사람 번호, 깊이)
while q:
    i, depth = q.popleft()
    if depth >= 2:
        continue
    
    for friend in relations[i]:
        if not visited[friend]:
            visited[friend] = True
            q.append((friend, depth+1))
            count += 1

print(count)