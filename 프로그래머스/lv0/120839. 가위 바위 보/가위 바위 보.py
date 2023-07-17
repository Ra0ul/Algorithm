def solution(rsp):
    """
    가위는 2 
    바위는 0 
    보는 5
    
    각 상성은 한가지 경우만 있음
    가위 일때 바위(0)
    바위 일때 보(5)
    보일 때 가위(2)
    """
    answer = ''
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        else:
            answer +="2"
    return answer