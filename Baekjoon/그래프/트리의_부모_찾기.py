import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# N = int(input())
# graph = [[] for _ in range(N+1)]

# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# parents = [0] * (N+1)

# def dfs(node, p):
#     parents[node] = p
#     for neighbor in graph[node]:
#         if parents[neighbor] == 0:
#             dfs(neighbor, node)

# dfs(1, 0)

# for i in range(2, N + 1):
#     print(parents[i])
input = sys.stdin.readline
N = int(input().strip())

graph = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if parents[neighbor] == 0:
                parents[neighbor] = node
                queue.append(neighbor)

bfs(1)

# def dfs(node, parent):
#     parents[node] = parent
#     for neighbor in graph[node]:
#         if parents[neighbor] == 0:
#             dfs(neighbor, node)

# dfs(1, 0)

for i in range(2, N + 1):
    print(parents[i])
