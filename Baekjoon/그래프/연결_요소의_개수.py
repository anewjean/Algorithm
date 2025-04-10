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