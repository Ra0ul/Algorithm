
def check(n):
    new_n = int(n**0.5+1)
    for i in range(2, new_n):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n + 1):    
        if check(i) == True:
            answer += 1
    return answer