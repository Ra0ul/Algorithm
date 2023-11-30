def solution(my_string, m, c):
    string = ''
    answer = ''
    lst = []
    
    count = 0
    for i, j in enumerate(my_string):
        if count != m:
            string += j
            count += 1
        else:
            lst.append(string)
            count = 0
            string =''
            string += j
            count += 1
            
    lst.append(string)
    print(lst)   
    
    for i in lst:
        answer += i[c-1]
            
    return answer