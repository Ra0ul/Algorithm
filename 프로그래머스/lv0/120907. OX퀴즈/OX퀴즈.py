def solution(quiz):
    answer = []
    
    for i in quiz:
        i_slice = i.split()
        
        if i_slice[1] == '+':
            left = int(i_slice[0]) + int(i_slice[2])
            right= int(i_slice[4])
            print(left, right)

        else:
            left = int(i_slice[0]) - int(i_slice[2])
            right = int(i_slice[4])
        
        if left == right:
            answer.append('O')
        else:
            answer.append('X')
    
    return answer    
    
  