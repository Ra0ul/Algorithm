def solution(my_string, s, e):
    if s == e:
        return my_string
    else:
        rev = ''
        # 문자열을 리스트에 넣으면 걍 떨어져서 들어감!
        b = list(my_string[s:e+1])
        #b = [i for i in my_string[s:e+1]]
        while b:
            rev += b.pop()
        
        answer = my_string[:s] + rev + my_string[e+1:]
        return answer