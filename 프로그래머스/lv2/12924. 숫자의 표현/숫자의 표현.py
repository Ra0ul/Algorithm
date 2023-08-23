def solution(n):
    answer = 0
    
    #시작하는 수 b
    for b in range(1,n+1):
        plus = []
        #연속하는 숫자의 갯수 i
        for i in range(0, n-b+1):
            if b == n:
                answer += 1
                break
            elif b+(b+1) >n:
                break
            else:
                plus.append(i+b)
                # print(plus)

                if sum(plus) == n:
                    answer += 1
                    break 
                elif sum(plus) > n:
                    break
                    
    # print("⭐️: ", answer)
    return answer