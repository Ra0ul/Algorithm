
"""
두명만 타기
구명보트 최대한 적게 모두 구출
"""
from collections import deque

def solution(people, limit):
    boat = 0
    new_list = deque(sorted(people))
    
    while new_list:
        
        if len(new_list) == 1:
            boat += 1
            break
            
        elif new_list[0] + new_list[-1] <= limit:
            new_list.popleft()
            boat +=1
            try:
                new_list.pop()
            except:
                pass
        
        else:
            new_list.pop()
            boat +=1
            # print(new_list, boat)
             
    return boat