from collections import deque
def solution(numLog):
    answer = ''
    numLog = deque(numLog)
    change = dict(zip([1,-1,10,-10], ['w','s','d','a']))

    num = numLog.popleft()
    while numLog:
        n_num = numLog.popleft()
        answer += change[n_num-num]
        num = n_num
    return answer