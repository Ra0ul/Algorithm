def solution(my_string, queries):
    answer = ''
    
    for i in queries:
        t_ = ''
        t = list(my_string[i[0]:i[1]+1])

        for _ in range(len(t)):
            t_ += t.pop()
        my_string = my_string[:i[0]] + t_ + my_string[i[1]+1:]
        
    
    return my_string