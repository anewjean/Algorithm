import sys

N = int(input())
An = []
An += list(map(int, input().split()))

visited = list(map(int, input().split()))
mapper = {0: lambda x: x[0] + x[1],
          1: lambda x: x[0] - x[1],
          2: lambda x: x[0] * x[1],
          3: lambda x: x[0] // x[1] if x[0] >= 0 else -(-x[0] // x[1])}

MAX = -sys.maxsize
MIN = sys.maxsize

def dfs(current_val: int, num_idx: int):
    global MAX, MIN
    
    if num_idx == N:
        MAX = max(MAX, current_val)
        MIN = min(MIN, current_val)
        return 
    
    for i in range(4):
        if visited[i] > 0:
            visited[i] -= 1
            result = mapper[i]((current_val, An[num_idx]))
            dfs(result, num_idx+1)
            visited[i] += 1

dfs(An[0], 1)
print(MAX)
print(MIN)