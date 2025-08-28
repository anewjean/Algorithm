import sys
input = sys.stdin.readline

X = int(input().strip())
total = input().strip()

len_w = 0
len_m = 0
count = 0
idx = 0
n = len(total)

while idx < n:
    curr = total[idx]

    # 바로 처리
    if curr == 'W' and abs((len_w + 1) - len_m) <= X:
        len_w += 1
        count += 1
        idx += 1
    elif curr == 'M' and abs(len_w - (len_m + 1)) <= X:
        len_m += 1
        count += 1
        idx += 1

    # 바로 처리 안 되면 인접한 1칸까지 확인
    elif idx + 1 < n and total[idx] != total[idx+1]:
        nxt = total[idx+1]
        if nxt == 'W' and abs((len_w + 1) - len_m) <= X:
            len_w += 1
            count += 1
            if curr == 'M' and abs(len_w - (len_m + 1)) <= X:
                len_m += 1
                count += 1
                idx += 2
            else: 
                break
        elif nxt == 'M' and abs(len_w - (len_m + 1)) <= X:
            len_m += 1
            count += 1
            if curr == 'W' and abs((len_w + 1) - len_m) <= X:
                len_w += 1
                count += 1
                idx += 2
            else: 
                break
        else: 
            break
    else:
        break

print(count)