def solution(quiz):
    answer = []
    for mathes in quiz:
        math_list = mathes.split()
        if math_list[1] == "-":
            left = int(math_list[0]) - int(math_list[2])
        else:
            left = int(math_list[0]) + int(math_list[2])
            
        right = int(math_list[4])
        
        if left == right:
            answer.append("O")
        else :
            answer.append("X")
    
    
    return answer