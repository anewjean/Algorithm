# 위상정렬
# in-degree가 0인 노드들을 모두 priority_q에 넣는다.
# 노드 = heapq.heapppop(q) 
# 노드와 연결된 이웃 노드들의 in-degree -= 1

import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

result = []
q = []

for i in range(1, N + 1):
    if in_degree[i] == 0:
        heapq.heappush(q, i)

while q:
    node = heapq.heappop(q)
    result.append(node)

    for neighbor in graph[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(q, neighbor)

print(*result)