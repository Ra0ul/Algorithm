def solution(my_string):
    answer = ''
    """
    중복된 문자 제거하기
    문자열을 돌면서 본인과 같은 문자열이 있으면 버리고
    없으면 answer에 더해주기!
    """
    count = 0
    # print(my_string[count+1:])
    for i in my_string:
        if i not in answer:
            answer += i
        else:
            pass
        count += 1
    return answer