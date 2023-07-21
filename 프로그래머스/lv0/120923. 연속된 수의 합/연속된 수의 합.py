def solution(num, total):
    answer = [] 
    num_list = 0
    
    for i in range(0, num):
        num_list += i 
    x = int((total - num_list)/num)
    for i in range(x,x+num):
        answer.append(i)
    return answer