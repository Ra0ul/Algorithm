answer = []
def collatz(n):
    if n == 1:
        answer.append(1)
        return answer
    else:
        answer.append(n)
        if n%2 == 0: 
            n=n//2
        else:
            n=3*n+1
        return collatz(n)
    
     


def solution(n):
    #x가 짝수는 2로 나누고
    #x가 홀수일 때는 3 * x + 1로 바꾸는 
    return collatz(n)