def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0

    for value in goal:
        if idx1 < len(cards1) and value == cards1[idx1]:
            idx1 += 1
        elif idx2 < len(cards2) and value == cards2[idx2]:
            idx2 += 1
        else:
            return False