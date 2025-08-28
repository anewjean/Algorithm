import sys

def cross(ax, ay, bx, by, cx, cy):
    return (bx-ax)*(cy-ay) - (by-ay)*(cx-ax)

def dist2(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return dx*dx + dy*dy

def solve():
    ax, ay = map(int, sys.stdin.readline().split())
    bx, by = map(int, sys.stdin.readline().split())
    cx, cy = map(int, sys.stdin.readline().split())

    # 1) 일직선이면 삼각형 아님
    if cross(ax, ay, bx, by, cx, cy) == 0:
        print("X")
        return

    # 2) 세 변의 제곱 길이
    s = [
        dist2(ax, ay, bx, by),
        dist2(bx, by, cx, cy),
        dist2(cx, cy, ax, ay),
    ]
    s.sort()  # s0 <= s1 <= s2
    s0, s1, s2 = s

    # 3) 정삼각형
    if s0 == s1 == s2:
        print("JungTriangle")
        return

    # 4) 각의 종류
    if s2 > s0 + s1:
        angle = "Dunkak"     # 둔각
    elif s2 == s0 + s1:
        angle = "Jikkak"     # 직각
    else:
        angle = "Yeahkak"    # 예각

    # 5) 이등변 여부
    is_iso = (s0 == s1) or (s1 == s2)
    print(angle + ("2Triangle" if is_iso else "Triangle"))

solve()