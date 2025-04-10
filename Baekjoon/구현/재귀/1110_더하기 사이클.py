def calc_new_N(NN):
    global count
    temp = int(NN[0]) + int(NN[1])
    if temp < 10:
        temp = "0" + str(temp)
    new_N = NN[1] + str(temp)[1]
    count += 1
    if N == new_N:
        return
    if new_N != N:
        return calc_new_N(new_N)

N = input()
if len(N) == 1:
    N = "0" + N

count = 0

calc_new_N(N)
print(count)