area = 250 * 250 * 0.5

x, y = map(int, input().split())

if x + y == 0:
    ax, ay = 125, 125

elif x > 0 and y > 0:
    if x > y:
        ax, ay = 0, 250 - (area / x)   # 정답은 y축 위
    else:
        ax, ay = 250 - (area / y), 0   # 정답은 x축 위

elif x < 125 and y == 0: # 오른변 왼쪽 절반
    # 정답은 빗변 위
    t = 250 - (area / (250 - x))
    ax, ay = t, 250 - t

elif x == 0 and y < 125: # 왼변 아래 절반
    # 정답은 빗변 위
    t = 250 - (area / (250 - y))
    ax, ay = 250 - t, t

elif y == 0: # 빗변의 오른쪽 절반
    ax, ay = 0, (area / x) # 정답은 y축 위

else: # 빗변 위쪽 절반
    ax, ay = (area / y), 0 # 정답은 x축 위

print(f"{ax:.2f} {ay:.2f}")