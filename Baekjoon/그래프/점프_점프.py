n = int(input())
stones = list(map(int, input().split()))
start = int(input())

def dfs(x):
    visited[x] = True
    for nx in (x - stones[x], x + stones[x]):
        if 0 <= nx < n and not visited[nx]:
            dfs(nx)

visited = [False] * n
dfs(start-1)

print(sum(visited))
