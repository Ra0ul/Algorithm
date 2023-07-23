def solution(num, k):
    answer = 0
    for i in enumerate(str(num)):
        if i[1] == str(k):
            return i[0]+1
    return -1
        
    