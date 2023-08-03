def solution(dots):
    answer = 0
    """
    기울기 = x값의 증가량/y값의 증가량
    1-2랑 3-4랑 비교
    1-3랑 2-4랑 비교
    1-4랑 2-3랑 비교
    """
    rule = [(0,1,2,3),(0,2,1,3),(0,3,1,2)]
    
    for i in rule:
        #i = (1,2,3,4)
        left_x_size = dots[i[0]][0] - dots[i[1]][0]
        left_y_size = dots[i[0]][1] - dots[i[1]][1]
        right_x_size = dots[i[2]][0] - dots[i[3]][0]
        right_y_size = dots[i[2]][1] - dots[i[3]][1]
        
        if left_x_size/left_y_size == right_x_size/right_y_size:
            return 1
        else:
            answer = 0
        
    return answer