def solution(a, b):
    answer = 0
    if a == b:
        return a
    else:
        start = min(a,b)
        end = max(a,b)
        for i in range(start, end+1):
            answer += i
    return answer