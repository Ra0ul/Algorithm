def solution(number):
    answer = 0
    num = str(number)
    for i in num:
        answer+=int(i)
    return answer%9