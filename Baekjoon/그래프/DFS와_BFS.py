from collections import deque

def dfs(start: int) -> None:
    visited = [False] * (N + 1)
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        
        if not visited[node]:
            visited[node] = True
            result.append(node)

            for neighbor in sorted(graph[node], reverse=True):
                if not visited[neighbor]:
                    stack.append(neighbor)
    
    print(*result)

# def dfs_recursive(node: int):
#     if visited[node]:
#         return
    
#     visited[node] = True
#     result.append(node)

#     for neighbor in sorted(graph[node]):
#         dfs(neighbor)

def bfs(start: int) -> None:
    visited = [False] * (N + 1)
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()

        if not visited[node]:
            visited[node] = True
            result.append(node)

            for neighbor in sorted(graph[node]):
                if not visited[neighbor]:
                    queue.append(neighbor)

    print(*result)    


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i) # 양방향 그래프이므로! 

dfs(V)
bfs(V)