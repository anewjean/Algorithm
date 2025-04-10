N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
def dfs(index, total):
    global count

    if index == N:
        return
    
    total += nums[index]

    if total == S:
        count += 1

    dfs(index + 1, total) # 현재 숫자를 선택하는 경우
    dfs(index + 1, total - nums[index]) # 현재 숫자를 선택하지 않는 경우


dfs(0, 0)
print(count)