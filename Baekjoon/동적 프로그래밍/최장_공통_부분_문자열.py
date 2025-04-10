def get_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))

    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i - 1]]
            if rank[sa[i]] != rank[sa[i - 1]] or \
               (rank[sa[i] + k] if sa[i] + k < n else -1) != \
               (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1):
                tmp[sa[i]] += 1
        rank = tmp[:]
        if max(rank) == n - 1:
            break
        k <<= 1
    return sa

def get_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i

    h = 0
    lcp = [0] * (n - 1)
    for i in range(n):
        if rank[i] == 0:
            continue
        j = sa[rank[i] - 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i] - 1] = h
        if h > 0:
            h -= 1
    return lcp

A = input().strip()
B = input().strip()

S = A + '#' + B + '$'  # 구분자 추가 (A, B를 명확히 구분)
sa = get_suffix_array(S)
lcp = get_lcp(S, sa)

max_len = 0
start_idx = 0
len_A = len(A)

for i in range(len(lcp)):
    a1, a2 = sa[i], sa[i + 1]

    # 하나는 A에서, 다른 하나는 B에서 시작해야 함
    if (a1 < len_A) != (a2 < len_A):
        if lcp[i] > max_len:
            max_len = lcp[i]
            start_idx = min(a1, a2)

print(max_len)
if max_len > 0:
    print(S[start_idx:start_idx + max_len])