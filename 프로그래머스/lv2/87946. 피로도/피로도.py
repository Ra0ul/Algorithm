
import itertools

def solution(k, dungeons):
    
    count_list = []
    ways = list(itertools.permutations(dungeons, len(dungeons)))
    
    for i in ways: #모든 경우의 수 검사
        count = 0
        power = k
        for u in i: #배열 순서대로 던전 통과
            if power >= u[0]:
                power -= u[1]
                count += 1
            else:
                break
        count_list.append(count)  #몇개 지났는지 저장
            
    return max(count_list) #가장 많이 지난 것은?