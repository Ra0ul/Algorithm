
def solution(s, skip, index):
    answer = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_alpha = ''
    
    for i in alpha:
        if i not in skip:
            new_alpha += i
    
    for i in s:
        num = (new_alpha.find(i) + index)%len(new_alpha)
        answer += new_alpha[num]
    
    return answer