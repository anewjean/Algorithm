import sys
input = sys.stdin.readline

# 부모를 찾는 함수 (경로 압축 포함)
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

# 두 집합을 합치는 함수
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parents[root_b] = root_a
        return True  # union 성공
    return False  # 이미 같은 집합

# 정점(V), 간선(E) 입력
V, E = map(int, input().split())

# 부모 배열 초기화
parents = [i for i in range(V + 1)]  # 정점 번호가 1부터 시작한다고 가정

# 간선 리스트 입력
edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))  # 비용 먼저 넣어야 정렬이 쉬움

# 1. 간선을 비용 기준으로 오름차순 정렬
edges.sort()

# 2. 간선을 하나씩 선택해가며 MST 구성
mst_cost = 0
for cost, a, b in edges:
    if union(a, b):  # 사이클이 없으면 추가
        mst_cost += cost

print(mst_cost)
