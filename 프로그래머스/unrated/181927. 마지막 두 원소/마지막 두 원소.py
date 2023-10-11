
def solution(num_list):
    num1 = num_list[-1]
    num2 = num_list[-2]
    if num1 > num2:
        answer = num1 -num2
    else:
        answer = num1*2
    num_list.append(answer)
    return num_list