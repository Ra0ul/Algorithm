def solution(s):
    answer = -1
    stack = []
    """
    두개 나오면 빼주기
    """
    for i in s:
        if i not in stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
        
        
    if stack:
        return 0
    else: 
        return 1