def solution(numbers):
    answer = -1
    x_numbers = [0,1,2,3,4,5,6,7,8,9]
    for i in numbers:
        x_numbers.remove(i)
    answer = sum(x_numbers)
    return answer