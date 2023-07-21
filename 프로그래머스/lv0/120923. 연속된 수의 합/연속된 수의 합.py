def solution(num, total):
    answer = [] 
    num_list = 0
    """
    연속한수 Num개
    더한값 total
    이되는 배열을 오름차순으로 담아 보내기!
    x, x+1,... x+(num-1)
    
    total = num*x + (0+1+2+3 ... + num-1)
    """
    for i in range(0, num):
        num_list += i 
    x = int((total - num_list)/num)
    for i in range(x,x+num):
        answer.append(i)
    return answer