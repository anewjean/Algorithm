wo, io, t = map(int, input().split()) # 초기값: 체중, e 섭취량(=기초대사량), 기초대사량 변화 역치 (*활동 대사량 = 0)
d, i, a = map(int, input().split()) # 다욧 중: 기간, e 섭취량, 활동 대사량

# 기초대사량 변화 고려 x
is_dead = False
bmr = io # 기초대사량
w = wo # 다욧 이후 체중

for _ in range(d):
    # 체중 변화
    w += (i - (bmr + a))
    # 사망 판별
    if (w <= 0) or (bmr <= 0):
        is_dead = True
        break
if is_dead:
    print("Danger Diet")
else:
    print(w, bmr)
    
# 기초대사량 변화
is_dead = False
yoyo_detected = False
bmr = io # 기초대사량
w = wo # 다욧 이후 체중

for _ in range(d):
    e_diff = i - (bmr + a)
    # 체중 변화
    w += e_diff
    # 기초대사량 변화
    if abs(e_diff) > t:
        bmr += (e_diff // 2)
    # 사망 판별
    if (w <= 0) or (bmr <= 0):
        is_dead = True
        break
# 요요 판별    
if bmr < io:
    yoyo_detected = True

if is_dead:
    print("Danger Diet")
else:
    print(w, bmr, "YOYO" if yoyo_detected else "NO")