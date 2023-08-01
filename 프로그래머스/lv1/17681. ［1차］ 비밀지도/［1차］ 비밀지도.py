def solution(n, arr1, arr2):
    answer = []
    map1=[]
    map2=[]
    secret_map=[]
    
    
    
    for i in arr1:
        map1.append(int(bin(i)[2:]))
    for i in arr2:
        map2.append(int(bin(i)[2:]))
    
    
    for i in range(n):
        secret_map.append(str(map1[i]+map2[i]))
        line =''
        if len(secret_map[i]) < n:
            blank = '0'*(n-len(secret_map[i]))
            secret_map[i] = blank+secret_map[i]
        for u in secret_map[i]:
            if int(u) >= 1:
                line += '#'
            else:
                line += ' '
        
        answer.append(line)
        
    return answer