def is_vps(ps: str) -> str:
    """
    vps가 아닌 경우
    1. ps의 요소들을 모두 순회한 후 stack에 요소가 남아있을 때
    2. ")"이 들어와서 pop 하는데 stack이 비어있을 때
    """
    stack = []
    for parenthesis in ps:
        if parenthesis == "(":
            stack.append(parenthesis)
        else:
            if not stack:
                print("NO")
                return
            stack.pop()
    if stack:
        print("NO")
    else:
        print("YES")