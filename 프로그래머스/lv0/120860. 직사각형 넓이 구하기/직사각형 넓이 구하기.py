def solution(dots):
    
    return(max(dots)[0]-min(dots)[0]) * (max(dots)[1]-min(dots)[1])
    
    
    # answer = 0
    # x_group=[]
    # y_group=[]
    # """
    # 직사각형의 넓이 =  가로*세로
    # 가로 = x 좌표의 차이 (dot에서 두값)
    # 세로 = y 좌표의 차이 (dot에서 두값)
    # """
    # for i in range(0,3):
    #     if dots[i][0] not in x_group:
    #         x_group.append(dots[i][0])
    #     if dots[i][1] not in y_group:
    #         y_group.append(dots[i][1])
    # answer = abs((x_group[0]-x_group[1])*(y_group[0]-y_group[1]))
    return 0