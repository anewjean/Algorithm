N = int(input())
matrix = [list(input()) for _ in range(N)]

def dfs(x: int, y: int, length: int) -> int:
    first_color = matrix[x][y]
    if length == 1:
        return first_color
    
    is_all_same = True
    for i in range(x, x + length):
        for j in range(y, y + length):
            if matrix[i][j] != first_color:
                is_all_same = False
                break
        if not is_all_same:
            break

    if is_all_same:
        return first_color
    else:
        half_length = length // 2
        LU = dfs(x, y, half_length)
        RU = dfs(x, y + half_length, half_length)
        LD = dfs(x + half_length, y, half_length)
        RD = dfs(x + half_length, y + half_length, half_length)
        return f"({LU}{RU}{LD}{RD})"

print(dfs(0, 0, N))
