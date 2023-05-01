def solution(s):
    answer = {}
    list = ''
    """
    딕셔너리로 정리해볼까?
    해당 글자를 key로 가지는 딕셔너리 value 값이 하나씩 올라가도록?
    
    value가 가장 작은 min 인 key 값을 구하고
    이걸 sort해서 순서대로 출력되게 만들어보기
    """
    s = sorted(s)
    
    for i in s:
        try:
            answer[i] += 1
        except:
            answer[i] = 1
    
    
    for key, value in answer.items():
        if value == 1:
            list += key     
            
    return list