def solution(num, k):
    answer = 0
    num, k = str(num), str(k)
    
    if k in num:
        answer = num.index(k)+1
    else:
        answer =-1
        
    return answer