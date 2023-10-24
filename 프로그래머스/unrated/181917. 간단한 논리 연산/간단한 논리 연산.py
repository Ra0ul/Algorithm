def solution(x1, x2, x3, x4):
    answer = True
    x1, x2, x3, x4 = map(int, [x1, x2, x3, x4])
    answer = (x1+x2)*(x3+x4)
    return bool(answer)