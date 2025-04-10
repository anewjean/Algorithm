from collections import deque

N, M, K, X = map(int, input().split())

# graph = [[0] * (N + 1) for _ in range(N + 1)]

# for _ in range(M):
#     A, B = map(int, input().split())
#     graph[A][B] = 1

# answer = []

# def dfs(node, count):
#     if count == K:
#         answer.append(node)
#         return

#     count += 1
#     for candidate, can_go in enumerate(graph[node]):
#         if can_go:
#             dfs(candidate, count)

# dfs(X, 0)
# answer.sort()

# if answer:
#     for i in answer:
#         print(i)
# else: 
#     print(-1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0

queue = deque([X])

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[node] + 1
            queue.append(neighbor)

found = False
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        found = True

if not found:
    print(-1)
