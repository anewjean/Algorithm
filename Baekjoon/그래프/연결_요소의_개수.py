###################################################### UNION FIND 풀이
N, M = map(int, input().split())
parents = [i for i in range(N + 1)]

def find(child: int) -> int:
    if child != parents[child]:
        parents[child] = find(parents[child])
    return parents[child]

def union(child_1: int, child_2: int) -> None:
    root_1 = find(child_1)
    root_2 = find(child_2)

    if root_1 != root_2:
        parents[root_1] = root_2
        for i in range(N + 1):
            if parents[i] == root_1:
                parents[i] = root_2

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

print(len(set(parents)) - 1)

##################################################### BFS 풀이
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)] # 1-based 인접리스트 풀이

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    # 무방향 그래프이므로 양방향으로 처리
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
cnt = 0

for i in range(1, n+1):
    if visited[i]:
        continue
    cnt += 1
    q = deque([i])
    visited[i] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)

print(cnt)