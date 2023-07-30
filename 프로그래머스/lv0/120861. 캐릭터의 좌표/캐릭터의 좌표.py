def solution(keyinput, board):
    limit = [board[0]//2,board[1]//2]
    answer = []
    x,y = 0, 0
    
    for i in keyinput:
        if i == "up":
            y = min(y+1, limit[1])
        if i == "down":
            y = max(y-1, -limit[1])
        if i == "right":
            x = min(x+1, limit[0])
        if i == "left":
            x = max(x-1, -limit[0])      
        
    answer = [x, y]
    
    return answer