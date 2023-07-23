def solution(my_string, num1, num2):
    answer = ''
    new_list = list(my_string)
    new_list[num1] = my_string[num2]
    new_list[num2] = my_string[num1]
    
    for i in new_list:
        answer += i
        
    return answer