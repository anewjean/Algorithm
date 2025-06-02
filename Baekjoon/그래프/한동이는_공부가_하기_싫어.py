def dfs(start, graph, visited):
    count = 0
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            count += 1
            stack.append(graph[node])
    return count

N = int(input())
graph = [0] * (N + 1) 
for i in range(1, N + 1):
    graph[i] = int(input())

max_count = 0
answer = 0
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    count = dfs(i, graph, visited)
    if count > max_count:
        max_count = count
        answer = i

print(answer)
