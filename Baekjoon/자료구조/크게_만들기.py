# N, K = map(int, input().split())
# num = input()
# stack = []
# max_num = max(num)
# max_num_idx = num.index(max_num)

# if N - K - 1 <= max_num_idx:
#     num = num[max_num_idx:]

# while len(stack) >= N - K:
#     for n in num:
#         if stack and stack[-1] < n:
#             stack.pop()
#         stack.append(n)

# print("".join(stack))


N, K = map(int, input().split())
num = input()
stack = []
to_remove = K

for n in num:
    while stack and to_remove > 0 and stack[-1] < n:
        stack.pop()
        to_remove -= 1
    stack.append(n)

if to_remove > 0:
    stack = stack[:-to_remove]

print("".join(stack))