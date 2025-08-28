import sys
input = sys.stdin.readline

def find_winner(robots) -> int:
    n = len(robots)
    alive = set(range(n))                # 살아있는 로봇 인덱스(0-based)
    rounds = len(robots[0])              # 모든 문자열 길이는 동일하다고 가정

    for r in range(rounds):
        hands = {robots[i][r] for i in alive}  # 이번 라운드 손동작 집합

        # 무효 라운드: 전부 같거나 셋 다 나온 경우
        if len(hands) in (1, 3):
            continue

        # 두 종류만 나온 경우 → 진 손동작 제거
        if hands == {'R', 'S'}:
            loser = 'S'
        elif hands == {'S', 'P'}:
            loser = 'P'
        else:  # {'P', 'R'}
            loser = 'R'

        alive = {i for i in alive if robots[i][r] != loser}

        if len(alive) == 1:              # 우승자 확정
            return next(iter(alive)) + 1 # 1-based

    return 0                              # 끝까지 우승자 단일화 실패

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    robots = [input().strip() for _ in range(n)]
    print(find_winner(robots))
