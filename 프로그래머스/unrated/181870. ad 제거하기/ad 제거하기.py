def solution(strArr):
    answer = []
    """
    배열중에서 'ad'  글자가 붙어있는 원소를 찾으면 무조건 제외해주기
    """
    
    for i in strArr:
        if i.find('ad') == -1:
            answer.append(i)
        
    return answer