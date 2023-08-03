from itertools import combinations

def solution(dots):
    answer = 0
    answer_list = []
    
    for i in combinations(dots,2):
        #i = (1,2,3,4)
        answer_list.append((i[0][1] - i[1][1]) /(i[0][0] - i[1][0]))
        
    print(answer_list)   # 012   -3-2-1
    for i in range(len(answer_list)//2):
    
        if answer_list[i] == answer_list[-(i+1)]:
            answer = 1
    return answer