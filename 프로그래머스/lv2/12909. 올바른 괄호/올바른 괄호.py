def solution(s):
    answer = True
    stack = [] 
    
    for i in s:
        if i =="(":
            stack.append("(")
        else:
            try: 
                stack.pop()
            except:
                return False
            
    if stack:
        return False

    return True