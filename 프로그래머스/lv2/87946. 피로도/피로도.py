
import itertools

def solution(k, dungeons):
    
    count_list = []
    ways = list(itertools.permutations(dungeons, len(dungeons)))
    ways.sort()
    
    for i in ways:
        count = 0
        power = k
        for u in i:
            if power >= u[0]:
                power -= u[1]
                count += 1
            else:
                break
        count_list.append(count)   
            
    return max(count_list)