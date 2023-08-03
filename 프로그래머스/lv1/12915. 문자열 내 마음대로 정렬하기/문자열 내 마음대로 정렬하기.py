def solution(strings, n):
    answer = []
    """
    비교대상되는 인덱스의 문자를 문자열 맨 앞에 하나 추가해서 정렬해보기!
    """
    for i_num, i in enumerate(strings):
        strings[i_num] = i[n]+i
    strings.sort()
    
    for i in strings:
        answer.append(i[1:])
    
            
    return answer