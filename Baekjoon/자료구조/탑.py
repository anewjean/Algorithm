# # N = int(input())
# # towers = list(map(int, input().split()))

# # # 너무 비효율적 & 답도 안 나옴;;

# # # def find_nearlest_taller_tower(reversed_towers: list) -> int:
# # #     curr_height = reversed_towers[0]
# # #     for reversed_idx, height in enumerate(reversed_towers):
# # #         if height > curr_height:
# # #             return len(towers) - 1 - reversed_idx
# # #     return 0

# # # for idx, tower in enumerate(towers):
# # #     print(find_nearlest_taller_tower(list(reversed(towers[:idx+1]))), end=' ')



# # for idx, tower in enumerate(towers):
# #     find_nearlest_taller_tower(idx - 1, tower)

# # def find_nearlest_taller_tower(idx: int) -> int:
# #     curr_height = towers[idx]
# #     for j in range(i - 1, -1, -1):
# #         if curr_height < towers[j]:
# #             return j + 1
# #     return 0

# # for i in range(N):
# #     print(find_nearlest_taller_tower(i), end=' ')



# N = int(input())
# towers = list(map(int, input().split()))

# def find_nearest_tallest_tower(idx: int) -> int:
#     height = towers[idx]
#     for j in range(idx - 1, -1, -1):
#         if towers[j] > height:
#             return j + 1
#     return 0

# for idx, tower in enumerate(towers):
#     print(find_nearest_tallest_tower(idx), end=" ")





# def find_nearest_taller_tower(idx: int) -> int:
#     curr_height = towers[idx]
#     for i in range(idx - 1, -1, -1):
#         if curr_height < towers[i]:
#             return i + 1
#     return 0

# N = int(input())
# towers = list(map(int, input().split()))

# for i in range(N):
#     print(find_nearest_taller_tower(i), end=" ")



# N = int(input())  # 5
# towers = list(map(int, input().split()))  # 6 9 5 7 4
# stack = []  #  현재 가장 높은 타워 인덱스
# answer = [0] * N  # [0, 0, 0, 0, 0]

# for i in range(N):
#     while stack and towers[stack[-1]] <= towers[i]: # 무슨 의미지?
#         stack.pop()
    
#     if stack: # 현재 건물보다 큰 건물이 있는 것!
#         answer[i] = stack[-1] + 1
    
#     stack.append(i) # 현재 타워의 인덱스를 stack에 넣는다.

# print(*answer)







N = int(input())
towers = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N):
    while stack and towers[i] > towers[stack[-1]]:
        # 가장 큰 건물이 남을 때까지 stack에 넣고 빼기 조건 구현 
        stack.pop()
    
    if stack:
        answer[i] = stack[-1] + 1

    stack.append(i)

print(*answer)















# def find_nearest_tallest_tower(idx: int) -> int:
#     height = towers[idx]
#     for j in range(idx - 1, -1, -1):  # ✅ 수정
#         if towers[j] > height:
#             return j + 1  # 1-based index
#     return 0

# N = int(input())
# towers = list(map(int, input().split()))

# for idx, tower in enumerate(towers):
#     print(find_nearest_tallest_tower(idx), end=" ")