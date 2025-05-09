from collections import deque

FLIPS = [
    0b111000000, # 첫 번째 행
    0b000111000, # 두 번째 행
    0b000000111, # 세 번째 행
    0b100100100, # 첫 번재 열
    0b010010010, # 두 번째 열
    0b001001001, # 세 번째 열
    0b100010001, # 왼쪽 위 -> 오른쪽 아래 대각선
    0b001010100 # 오른쪽 위 -> 왼쪽 아래 대각선
]

def to_bitmask(coins):
    # 3 x 3 coins를 비트마스크로 변환 
    bitmask = 0
    for i in range(3):
        for j in range(3):
            if coins[i][j] == 'T':
                bitmask |= (1 << (3 * i  + j))
    return bitmask

def bfs(start):
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        state, flips = queue.popleft()

        if state == 0 or state == 0b111111111:
            return flips
        
        for flip_mask in FLIPS:
            new_state = state ^ flip_mask
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, flips + 1))
    
    return -1

def play_coin_game(coins):
    start = to_bitmask(coins)
    return bfs(start)

T = int(input())
for _ in range(T):
    coins = [input().split() for _ in range(3)]
    print(play_coin_game(coins))

# 몇 번 실패해야 -1을 반환할까?
