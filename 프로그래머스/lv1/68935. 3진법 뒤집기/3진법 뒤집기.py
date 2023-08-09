def solution(n):
    answer = 0
    trit = ''
    
    # 삼진법으로 전환
    while(n>2):
        trit +=  str(n%3)
        n = n//3
    
    # 다시 십진법으로 전환
    trit += str(n)
    return int(trit,3)