from collections import Counter

def find(child: int) -> int:
    if child != parents[child]:
        parents[child] = find(parents[child])
    return parents[child]

def union(child_1: int, child_2: int) -> None:
    root_1 = find(child_1)
    root_2 = find(child_2)

    if root_1 != root_2:
        c = max(root_1, root_2)
        p = min(root_1, root_2)
        parents[c] = p

N = int(input())
M = int(input())

parents = [i for i in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

# 모든 노드의 루트를 한 번씩 찾아서 경로 압축 완료
# for i in range(1, N + 1):
#     find(i)
for p in parents:
    find(p)

print(Counter(parents)[1] - 1)