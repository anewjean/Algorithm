parentheses = input()

def calc_val_of_parentheses(parentheses):
    stack = []
    temp = 1
    answer = 0
    
    for idx, parenthesis in enumerate(parentheses):
        if parenthesis == "(": 
            stack.append(parenthesis)
            temp *= 2
        elif parenthesis == "[":
            stack.append(parenthesis)
            temp *= 3
        elif parenthesis == ")":
            if not stack or stack[-1] != "(":
                return 0
            if parenthesis[idx-1] == "(":
                answer += temp
            stack.pop()
            temp //= 2
        elif parenthesis == "]":
            if not stack or stack[-1] != "[":
                return 0
            if parentheses[idx-1] == "[":
                answer += temp
            stack.pop()
            temp //= 3
        return answer if not stack else 0
    
print(calc_val_of_parentheses(parentheses))