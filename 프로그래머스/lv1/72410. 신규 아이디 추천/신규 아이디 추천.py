def solution(new_id):
    """
    1) lower() : 모두 소문자로 치환
    2) 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표 만 살리기
    3) 마침표 연속이면 다음 마침표는 삭제
    4) [0]이나 [-1]에 마침표면 삭제
    5) len(new_id) = 0이면 "a" 추가
    6) len(new_id) >= 16이면 [:15]까지만 유효
        if [0] 이나  [-1]에 마침표면 삭제
    7) len(new_id) <= 2이면 new_id[-1]를 len(new_id) = 3 될때까지 반복해서 붙인다
    """
    answer = ''
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num = ['0','1','2','3','4','5','6','7','8','9']
    extra = ['-','_','.']
    result_id = ''

    #1
    new_id = new_id.lower()

    #2
    for i in new_id:
        if (i in alpha) or (i in num) or (i in extra):
            result_id += i
    
    #3
    while('..' in result_id):
        result_id = result_id.replace('..', '.')
         
    #4
    if (result_id[0] == '.'):
        result_id = result_id[1:]
    try:
        if (result_id[-1] == '.'):
            result_id = result_id[:-1]
    except:
        pass
       
    #5
    if len(result_id) == 0:
        result_id += 'a'
    
    #6
    elif len(result_id) >= 16:
        result_id = result_id[:15]
        if (result_id[-1] == '.'):
            result_id = result_id[:-1]
            
    #7
    while len(result_id) <= 2:
        result_id += result_id[-1]
    
    return result_id