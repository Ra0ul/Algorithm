def solution(a, b, c):
    check = len(set([a,b,c]))
    if check == 3:
        answer = a+b+c
    elif check == 2:
        answer = (a + b + c) * (a**2 + b**2 + c**2 )
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
    
    return answer