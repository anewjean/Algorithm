import sys

def is_acceptable(pw: str) -> bool:
    mos = ('a', 'e', 'i', 'o', 'u')
    
    # a, e, i, o, u 중 하나라도 없으면 X
    if not any(p in mos for p in pw):
        return False
    
    mo = 0
    ja = 0
    prev = ""
    
    for p in pw:    
        # 모음 3개 연속 또는 자음 3개 연속으로 오면 X
        if p in mos:
            mo += 1
            ja = 0
        else:
            mo = 0
            ja += 1
        
        if mo == 3 or ja == 3:
            return False
        
        # ee, oo 제외하고 같은 글자 2개 연속으로 오면 X
        if prev == p and p not in ('e', 'o'):
            return False
        prev = p
    
    return True

for pw in iter(input, "end"):
    pw = pw.strip()
    result = "acceptable" if is_acceptable(pw) else "not acceptable"
    print(f"<{pw}> is {result}.")
