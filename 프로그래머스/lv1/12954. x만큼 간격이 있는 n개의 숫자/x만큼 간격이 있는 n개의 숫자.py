def solution(x, n):
    answer = []
    for i in range(n+1):
        answer.append(i*x)
        
    # if x != 0:
    answer.remove(0)
        
    return answer