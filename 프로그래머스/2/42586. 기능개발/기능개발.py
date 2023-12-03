
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