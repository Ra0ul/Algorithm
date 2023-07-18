def solution(my_string):
    answer = []
    """
    1. 숫자만 먼저 뽑기
    2. 숫자를 오름차순 정렬하기
    
    """
    for i in my_string:
        if i.isalpha() != True:
            answer.append(int(i))
    answer.sort()
    return answer