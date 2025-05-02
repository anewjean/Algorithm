N, M = map(int, input().split())
trains = [0] * N

for _ in range(M):
    num, train_num, *passenger_num = map(int, input().split())
    
    if (num == 1): # 탑승
        p = passenger_num[0] - 1
        trains[train_num-1] |= (1 << p) 

    elif (num == 2): # 하차
        p = passenger_num[0] - 1
        trains[train_num-1] &= ~(1 << p) 

    elif (num == 3): # 뒤로
        trains[train_num-1] <<= 1
        trains[train_num-1] &= (1<<20) - 1

    elif (num == 4): # 앞으로
        trains[train_num-1] >>= 1
        
print(len(set(trains)))
