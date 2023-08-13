import itertools

def check(n):
    new_n = int(n**0.5+1)
    for i in range(2, new_n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    select = list(itertools.combinations(nums,3))
    
    for i in select:
        if check(sum(i)):
            answer += 1
    return answer