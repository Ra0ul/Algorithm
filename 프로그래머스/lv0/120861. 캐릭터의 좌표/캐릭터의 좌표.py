def solution(keyinput, board):
    limit = [board[0]//2,board[1]//2]
    answer = []
    x_pos = []
    y_pos = []
    
    for i in keyinput:
        if i == "up":
            y_pos.append(1)
            if abs(sum(y_pos)) > limit[1]:
                y_pos.remove(1)
        if i == "down":
            y_pos.append(-1)
            
            if abs(sum(y_pos)) > limit[1]:
                y_pos.remove(-1)
        if i == "right":
            x_pos.append(1)
            if abs(sum(x_pos)) > limit[0]:
                x_pos.remove(1)
        if i == "left":
            x_pos.append(-1)
            if abs(sum(x_pos)) > limit[0]:
                x_pos.remove(-1)           
    answer = [sum(x_pos), sum(y_pos)]
    
    return answer