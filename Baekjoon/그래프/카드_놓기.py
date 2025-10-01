# 풀이1. permutation 모듈 이용
# from itertools import permutations

# n = int(input())
# k = int(input())
# cards = [input().strip() for _ in range(n)]
# perm = permutations(cards, k)
# answer = set(int("".join(p)) for p in perm)
# print(len(answer))

# 풀이2. DFS + 백트래킹으로 직접 순열 생성
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
used = [False] * n
answer = set()

def dfs(path):
    if len(path) == k:
        answer.add("".join(path))
        return
    for i in range(n):
        if not used[i]:
            used[i] = True
            dfs(path + [cards[i]])
            used[i] = False # 백트래킹
        
dfs([])
print(len(answer))