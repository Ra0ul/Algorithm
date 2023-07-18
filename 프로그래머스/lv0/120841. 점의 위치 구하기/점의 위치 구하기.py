def solution(dot):
    answer = 0
    """
    양양 = 1
    음양 = 2
    음음 = 3
    양음 = 4
    """
    quad = [(1,4),(2,3)]
    answer = quad[dot[0]<0][dot[1]<0]
 
    return answer