def  win_ttt(board, piece):
    # 위치 벡터 (→, ↓, ↘︎, 왼쪽 아래)
    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]
    
    # 첫 번째 piece 위치 찾기
    i_1 = j_1 = 0
    while board[i_1][j_1] != piece and i_1 < 2 and j_1 < 2:
        i_1 += 1
        j_1 += 1
    
    # 두 번째 piece 위치 찾기
    for d in range(4):
        i_2 = i_1 + dx[d]
        j_2 = j_1 + dy[d]
        if board[i_2][j_2] == piece:
            break
    
    # 두 번째 piece의 열 위치에 따라 이기는 판 반환
    if j_2 == 2: # 마지막 열이라면 방향 벡터 반대로
        i_3 = i_1 - dx[d]
        j_3 = j_1 - dy[d]
    else: # 두번째 열이라면 방향 벡터 동일하게
        i_3 - i_2 + dx[d]
        i_3 - i_2 + dy[d]
    
    board[i_3][j_3] = piece
    return board
    
N = int(input())
for n in range(1, N+1):
    board = [input() for _ in range(3)]
    piece = input()
    print(f"Case {n}: ")
    print(win_ttt(board, piece))
