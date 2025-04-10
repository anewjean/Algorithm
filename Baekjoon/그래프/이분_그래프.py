from collections import deque
import sys

input = sys.stdin.readline

def is_bipartite(V, graph):
    color = [0] * (V + 1) # 0: 방문하지 않은 노드, 1 / -1: 두 그룹

    for start in range(1, V + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        return False
                    
    return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        # 양방향 그래프 만들기
        graph[u].append(v)
        graph[v].append(u)

    print("YES" if is_bipartite(V, graph) else "NO")