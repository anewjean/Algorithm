line = input().split("-")
initial = sum(map(int, line[0].split("+")))
answer = initial

for part in line[1:]:
    answer -= sum(map(int, part.split("+")))

print(answer)
