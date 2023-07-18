def solution(numbers):
    
    #number 에서 큰 두 개 값을 뽑기
    answer = sorted(numbers, reverse=True)
    #그 두개를 곱하기
    answer = answer[0]*answer[1]
    
    
    return answer