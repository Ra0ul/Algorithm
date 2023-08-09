"""

def bill(num, m, score):  #0,1,2,3 ...,m
    for i in range(0,num,m):
        price += min(score[i:i+m])*m
    return price
    
"""

def solution(k, m, score):
    answer = 0
    price = 0
    tray =[]
    """
    비싼건 최대한 비싼것 끼리 모으기!
    """
    score.sort(reverse=True)
    # print("원본 : ", score)
    # 과일 수가 딱 떨어지면
    if len(score)%m == 0:
        # print(bill(len(score), m, score))
        for i in range(0,len(score),m):
            price += min(score[i:i+m])*m
        return price
    # 과일 수가 안 떨어지면
    else:
        for i in range(0, len(score)-len(score)%m,m):
            price += min(score[i:i+m])*m
        return price