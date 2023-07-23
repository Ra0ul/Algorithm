def solution(num_list, n):
    answer = []
    index = 0    


    for i in range(0,len(num_list)//n):
        answer.append(num_list[index:index+n])
        index += n
    print(answer)
    
    
    return answer