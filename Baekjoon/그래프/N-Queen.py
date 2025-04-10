N = int(input())
arr = [0] * N 

def is_possible(r):
    for i in range(r):
        if arr[r] == arr[i]:
            return False
        if r - i == abs(arr[r] - arr[i]):
            return False
    return True

def dfs_2(row):
    if row == N:
        return 1
    
    ans = 0
    for i in range(N):
        arr[row] = i
        if is_possible(row):
            ans += dfs(row + 1)
    
    return ans

print(dfs_2(0))

#############################################################
N = int(input())
arr = [[0] * N for _ in range(N)]

def dfs(row):
    if row == N: # 종료 조건
        return 1 # 전체 row를 탐색하고 정상 배치했다면 1 리턴
    
    ans = 0
    for col in range(N): # 전체 행을 돌면서 퀸 배치
        if is_possible(row, col):
            arr[row][col] = 1 # (row, col)에 퀸 배치
            ans += dfs(row + 1) # 다음 row 확인
            arr[row][col] = 0 # (row, col) 초기화
    return ans

def is_possible(r, c):
    for i in range(r):
        if arr[i][c] == 1: # 모든 열 확인
            return False
    
    i, j = r - 1, c - 1
    while 0 <= i and 0 <= j:
        if arr[i][j] == 1: # 좌측 상단 확인
            return False
        i -= 1 
        j -= 1 
    
    i, j = r - 1, c + 1
    while 0 <= i and j < N:
        if arr[i][j] == 1: # 우측 상단 확인
            return False
        i -= 1
        j += 1

    return True

print(dfs(0))
