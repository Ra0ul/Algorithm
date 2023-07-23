def solution(my_string, num1, num2):
    new_list = list(my_string)
    new_list[num1], new_list[num2] = new_list[num2], new_list[num1]
        
    return ''.join(new_list)