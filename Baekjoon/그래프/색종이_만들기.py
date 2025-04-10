N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

color_count = {0: 0,
               1: 0}

def dfs(x, y, length):
    global color_count
    color = matrix[x][y]

    if length < 1:
        return
    
    is_indivisible = True

    for i in range(x, x + length):
        for j in range(y, y + length):
            if matrix[i][j] != color:
                is_indivisible = False
                break

    if is_indivisible:
        color_count[color] += 1
    else:
        half = length // 2
        dfs(x, y, half)
        dfs(x + half, y, half)
        dfs(x, y + half, half)
        dfs(x + half, y + half, half)
    
dfs(0, 0, N)

print(color_count[0])
print(color_count[1])