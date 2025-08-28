from itertools import combinations
import sys
input = sys.stdin.readline

X = input().strip()
Y = input().strip()
Z = input().strip()
k = int(input())

def make_cmb_set(s, k):
    return {''.join(val) for val in combinations(s, k)}

cx = make_cmb_set(X, k)
cy = make_cmb_set(Y, k)
cz = make_cmb_set(Z, k)

answer = sorted((cx & cy) | (cy & cz) | (cz & cx))
if answer:
    for val in answer:
        print(val)
else:
    print(-1)
