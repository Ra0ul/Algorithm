def solution(a, d, included):
    stack = []
    for i in range(len(included)):
        answer = a+d*i
        if included[i]:
            stack.append(answer)
        
    return sum(stack)