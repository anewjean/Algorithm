from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def calc_r(A):
    max_len = 0
    new_A = []

    for row in A:
        count = Counter(row)
        del count[0] # 0 무시
        sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]))
        new_row = []
        for num, cnt in sorted_items:
            new_row.extend([num, cnt])
        max_len = max(max_len, len(new_row))
        new_A.append(new_row)
    # 남는 부분 0 채우고 100개까지만 남기기
    for row in new_A:
        row += [0] * (max_len - len(row))
        if len(row) > 100:
            row[:] = row[:100]
    return new_A 

def calc_c(A):
    transsposed = list(map(list, zip(*A)))
    transsposed = calc_r(transsposed)
    return list(map(list, zip(*transsposed)))

time = 0
while time <= 100:
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]) and A[r-1][c-1] == k:
        print(time)
        break
    if len(A) >= len(A[0]):
        A = calc_r(A)
    else:
        A = calc_c(A)
    time += 1
else: 
    print(-1)