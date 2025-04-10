def explode_recursive(string: str, bomb: str) -> str:
    if bomb not in string: 
        return string
    string = string.replace(bomb, "")
    return explode_recursive(string, bomb)

def explode(string: str, bomb: str) -> str:
    stack = []
    bomb_len = len(bomb)

    for s in string:
        stack.append(s)

        if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
            del stack[-bomb_len:]
    
    return  ''.join(stack) if stack else 'FRULA'

string = input()
bomb = input()
print(explode(string, bomb))