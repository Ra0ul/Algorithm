"""
progresses : 진도가 적힌 정수 배열
speeds : 작업 개발 속도
return : 각 배포마다 몇개의 기능이 배포되는지

배포는 하루에 한번만

1. 일단 남은 작업량을 계산
2. 일 진행하는 속도에 따라 
3. 배포할 수 있는 날짜 정리하기

"""
from collections import deque

def solution(progresses, speeds):
    answer = []
    state = deque()
    
    # 남은 일의 양
    for i_num, i in enumerate(progresses):
        quot = (100-i)//speeds[i_num]
        remain = (100-i)%speeds[i_num]
        if remain != 0:
            quot += 1
        state.append(quot)
        
    count = 1
    func = state.popleft()
    while state:
        
        if state[0] <= func:
            state.popleft()
            count += 1
            
        elif state[0] > func:
            func = state.popleft()
            answer.append(count)
            count = 1
        #print(state, count, answer, func)    
    answer.append(count)
    #print("here : ", answer )
    return answer