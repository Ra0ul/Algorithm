def solution(food):
    answer = ''
    """
    음식은 좌우로 대칭(홀수개는 하나 버리기), 가운데에는 물하나
    """
    for i in range(1, len(food)):
        num = food[i]//2
        answer += str(i)*num
    answer += ('0'+answer[::-1])  
    return answer